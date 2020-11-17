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
		self.cursor.execute(sqlQuery, items)

		self.mydb.commit()

	def gettingData(self):
		sqlQuery = "SELECT * FROM stdrecord"  # getting all attribute from Table
		self.cursor.execute(sqlQuery)
		rows = self.cursor.fetchall()
		return rows

