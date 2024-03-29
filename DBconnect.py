import mysql.connector
import datetime

class DB_connect():
	database=""
	table = ""
	isConnectDB = bool()
	def __init__(self, hostName, userName, passsword):
		# default connected database
		self.hostName = hostName
		self.userName = userName
		self.passsword = passsword
		try:
			self.mydb = mysql.connector.connect(host=self.hostName, user=self.userName, passwd=self.passsword)
			self.cursor = self.mydb.cursor()
			self.isConnectDB = True
		except mysql.connector.errors.DatabaseError:
			self.isConnectDB = False


	def addIntoDB(self, items: list):
		'''Add tuples into a Database 
		gender, contact, dob, address, rollnum, first_name, last_name, email'''
		# items = ('Male', '1234567890', '2000-01-01', '123 Main St', 101, 'John', 'Doe', 'john@example.com')
		status = None
		try:
			# Convert the date format to 'YYYY-MM-DD'
			dob = datetime.datetime.strptime(items[2], '%d/%m/%Y').strftime('%Y-%m-%d')
			# Insert into Basic table
			basic_query = f"INSERT INTO {self.table}Basic (gender, contact, dob, address) VALUES (%s, %s, %s, %s)"
			basic_values = (items[0], items[1], dob, items[3])
			self.cursor.execute(basic_query, basic_values)

			# Get the last inserted Basic id
			self.cursor.execute("SELECT LAST_INSERT_ID()")
			basic_id = self.cursor.fetchone()[0]

			# Insert into Record table
			record_query = f"INSERT INTO {self.table} (rollnum, first_name, last_name, email, basic_id) VALUES (%s, %s, %s, %s, %s)"
			record_values = items[4: ]
			record_values.append(basic_id)
			self.cursor.execute(record_query, record_values)

			# Commit the transaction
			self.mydb.commit()
			status = 1
		except mysql.connector.errors.IntegrityError:
			# if  primary key is already exist so data insertion is not possible
			status = 2
		except mysql.connector.Error as err:
			# Rollback on error
			self.mydb.rollback()
			status = 3
		
		return status 
		
	def gettingData(self):
		'''getting all attribute from Table'''
		selectAllQuery = f"""SELECT r.rollnum, r.first_name, r.last_name, r.email, b.gender, b.contact, b.dob, b.address
				FROM {self.table} as r
				JOIN {self.table}Basic as b ON r.basic_id = b.id ORDER BY r.rollnum;"""
		selectAllQuery.replace('\n', ' ')
		self.cursor.execute(selectAllQuery)
		return self.cursor.fetchall()
		

	def updateData(self, items: tuple):
		#('NewGender', 'NewContact', 'NewDOB', 'NewAddress', 101, 'NewFirstName', 'NewLastName', 'new_email@example.com', 101)
		updateQuery1 = f"UPDATE {self.table}Basic as b\
            JOIN {self.table} AS r ON b.id = r.basic_id\
            SET b.gender = %s,\
                b.contact = %s,\
                b.dob = %s,\
                b.address = %s\
            WHERE r.rollnum = %s;".replace("\n", " ")
		self.cursor.execute(updateQuery1, items[:5])
		
		updateQuery2 = f"UPDATE {self.table}\
				SET first_name = %s,\
                last_name = %s,\
                email = %s\
            	WHERE rollnum = %s;".replace("\n", " ")
		self.cursor.execute(updateQuery2, items[5:])
		self.mydb.commit()

	def deleteData(self, key: int):

		deleteQuery = (
			f"DELETE FROM {self.table} WHERE rollnum = {key}; ",
			f"DELETE FROM {self.table}Basic WHERE id NOT IN (SELECT DISTINCT basic_id FROM {self.table}); "
		)
		# in python we can't execute multiple SQL queries at once that is why iterating each of them
		for delQ in deleteQuery:
			self.cursor.execute(delQ)
		self.mydb.commit()

	def searchByFetch(self, searchBy, searchTxt):
		# Fetch the data from the database
		searchQuery = f"SELECT r.rollnum, r.first_name, r.last_name, r.email, b.gender, b.contact, b.dob, b.address FROM {self.table} as r\
				JOIN {self.table}Basic as b ON r.basic_id = b.id\
				WHERE {str(searchBy)} LIKE '%{str(searchTxt)}%'".replace("\n", " ")
		
		self.cursor.execute(searchQuery)
		return self.cursor.fetchall()

	def shows(self, whichSet: str):
		sqlQuery = f"SHOW {whichSet}"
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()

	def showTables(self):
		sqlQuery = "SHOW TABLES"
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()

	def useOtherDB(self):
		sqlQuery = f"USE {self.database}"
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

	def createDB(self,dbName):
		self.database = dbName
		print(type(self.database))
		sqlQuery = f"CREATE DATABASE IF NOT EXISTS {self.database}"
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

	def createtable(self, tableName):
		"""
		Creates two connected tables in the database: {tableName}Basic and {tableName}.
		{tableName}Basic stores ID, gender, contact, DOB, and address.
		{tableName} stores roll number, names, email, and links to {tableName}Basic.
		"""
		self.table = tableName
		sqlQuery = f'CREATE TABLE IF NOT EXISTS {self.table}Basic (\
					id INT AUTO_INCREMENT PRIMARY KEY,\
					gender VARCHAR(10),\
					contact VARCHAR(15),\
					dob DATE,\
					address VARCHAR(30)\
				);'
		self.cursor.execute(sqlQuery)
		sqlQuery = f'CREATE TABLE IF NOT EXISTS {self.table}(\
					rollnum INT PRIMARY KEY,\
					first_name VARCHAR(20),\
					last_name VARCHAR(20),\
					email VARCHAR(30),\
					basic_id INT,\
					FOREIGN KEY (basic_id) REFERENCES {self.table}Basic(id)\
				);'
		self.cursor.execute(sqlQuery)
		self.mydb.commit()
	
	def deleteTable(self, tableName):
		sqlQuery = f'DROP TABLE IF EXISTS {tableName}'
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

	def deleteDB(self, dbName):
		sqlQuery = f'DROP DATABASE IF EXISTS {dbName}'
		self.cursor.execute(sqlQuery)
		self.mydb.commit()