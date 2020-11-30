import mysql.connector

class DB_connect():
	database=""
	def __init__(self, hostName, userName, passsword):
		# default connected database
		self.hostName = hostName
		self.userName = userName
		self.passsword = passsword
		self.mydb = mysql.connector.connect(host=self.hostName, user=self.userName, passwd=self.passsword)

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

	def showDBs(self):
		sqlQuery = "SHOW DATABASES"
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()

	def showTables(self):
		sqlQuery = "SHOW Tables"
		self.cursor.execute(sqlQuery)
		return self.cursor.fetchall()

	def useOtherDB(self):
		sqlQuery = "USE %s"
		self.cursor.execute(sqlQuery, self.database)

	def createDB(self,dbName):
		self.database = dbName
		print(type(self.database))
		sqlQuery = f"CREATE DATABASE IF NOT EXISTS {self.database}"
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

	def createtable(self, tableName):
		sqlQuery = f"CREATE TABLE IF NOT EXISTS {tableName}"

