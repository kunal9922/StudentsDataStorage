import mysql.connector


class DB_connect():
	database="do"
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
		sqlQuery = f"CREATE TABLE IF NOT EXISTS {tableName}( RollNum INT(12) PRIMARY KEY, Name varchar(30) NOT NULL, Contact varchar(10), Email varchar(40), Gender varchar(6), DOB varchar(10), Adress varchar(80))"
		self.cursor.execute(sqlQuery)
		self.mydb.commit()

