import mysql.connector

class DB_connect():
	def __init__(self):
		self.hostName = "localhost"
		self.userName = "root"
		self.passsword = "kunal9922soni"
		self.dbName = "studentRecordtest"
		cmydb = mysql.connector.connect(host=self.hostName, user=self.userName, passwd=self.passsword, database = self.dbName )