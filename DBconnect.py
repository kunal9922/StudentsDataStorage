import mysql.connector


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


	def addIntoDB(self, items: tuple):
		'''gender, contact, dob, address, rollnum, first_name, last_name, email'''
		# items = ('Male', '1234567890', '2000-01-01', '123 Main St', 101, 'John', 'Doe', 'john@example.com')
		#query to insert into DB table
		sqlQuery = f"BEGIN; -- Start the transaction\
			-- Insert into Basic table\
			INSERT INTO {self.table}Basic (gender, contact, dob, address)\
			VALUES (%s, %s, %s, %s);\
			-- Get the last inserted Basic id\
			SET @basic_id = LAST_INSERT_ID();\
			-- Insert into Record table\
			INSERT INTO {self.table} (rollnum, first_name, last_name, email, basic_id)\
			VALUES (%s, %s, %s, %s, @basic_id);\
			COMMIT; -- Commit the transaction"
		try:
			self.cursor.execute(sqlQuery, items)
			self.mydb.commit()
			return True

		except mysql.connector.errors.IntegrityError:
			# if  primary key is already exist so data insertion is not possible
			return False

	def gettingData(self):
		sqlQuery = f"SELECT r.rollnum, r.first_name, r.last_name, r.email, b.gender, b.contact, b.dob, b.address\
				FROM {self.table} r\
				JOIN {self.table}Basic b ON r.basic_id = b.id;"
		# getting all attribute from Table
		print(sqlQuery)
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()
		

	def updateData(self, items: tuple):
		sqlQuery = f"BEGIN; -- Start the transaction\
			UPDATE {self.table}Basic as b\
			JOIN {self.table} AS r ON b.id = r.basic_id\
			SET b.gender = %s,\
				b.contact = %s,\
				b.dob = %s, -- New value for dob\
				b.address = %s\
			WHERE r.rollnum = %s; -- Use the appropriate condition to identify the record in the Basic table\
			UPDATE {self.table}\
			SET first_name = %s,\
				last_name = %s,\
				email = %s,\
			WHERE rollnum = %s; -- Use the appropriate condition to identify the record in the Record table\
			COMMIT; -- Commit the transaction"
		self.cursor.execute(sqlQuery, items)
		self.mydb.commit()

	def deleteData(self, key: int):

		sqlQuery = f"BEGIN; -- Start the transaction\
			-- Delete from Record table\
			DELETE FROM {self.table} WHERE rollnum = %s; -- Use the appropriate condition to identify the record in the Record table\
			-- Delete associated Basic data\
			DELETE FROM {self.table}Basic WHERE id NOT IN (SELECT basic_id FROM {self.table});\
			COMMIT; -- Commit the transaction\
			"
		print(sqlQuery)
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

	def searchByFetch(self, sqlQuery):
		self.cursor.execute(sqlQuery)
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
					id INT PRIMARY KEY,\
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