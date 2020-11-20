import mysql.connector

class DB_connect():
	def __init__(self):
		# default connected database
		self.hostName = "localhost"
		self.userName = "root"
		self.passsword = "kunal9922soni"
		self.dbName = "studentRecordtest"
		self.mydb = mysql.connector.connect(host=self.hostName, user=self.userName, passwd=self.passsword, database=self.dbName)

		self.cursor = self.mydb.cursor()

	def addIntoDB(self, items: tuple):
		'''Rollnum, Name, contact, Email, Gender, DOB, Address'''
		#query to insert into DB table
		sqlQuery = "INSERT INTO stdrecord values(%s, %s, %s, %s, %s, %s, %s )"

		try:
			self.cursor.execute(sqlQuery, items)
			self.mydb.commit()
			return True

		except mysql.connector.errors.IntegrityError:
			# if  primary key is already exist so data insertion is not possible
			return False

	def gettingData(self):
		sqlQuery = "SELECT * FROM stdrecord"  # getting all attribute from Table
		self.cursor.execute(sqlQuery)
		rows = self.cursor.fetchall()
		return rows

	def updateData(self, items: tuple):
		sqlQuery = "UPDATE stdrecord SET RollNum=%s, Name=%s, Contact=%s, Email=%s, Gender=%s, DOB=%s, Adress=%s WHERE RollNum=%s"
		self.cursor.execute(sqlQuery, items)
		self.mydb.commit()

	def deleteData(self, key: int):

		sqlQuery = "DELETE FROM stdrecord WHERE RollNum=%s"
		self.cursor.execute(sqlQuery, key)
		self.mydb.commit()

	def searchByFetch(self, sqlQuery):
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()