import tkinter as tk
from tkinter.font import Font
import DBconnect
from tkinter import messagebox
from student import StudentManagementSystem
class ShowDBFrame():
	def __init__(self):
		self.hostName = ""
		self.userName = ""
		self.passwrd = ""
		self.DB = None

	count = 0 # count no. of studentEXE frame created
	def InfoInput(self, rootWin, hostName, userName, password):

		# storing user login info for futher uses
		self.hostName = hostName
		self.userName = userName
		self.passwrd = password

		self.DB = DBconnect.DB_connect(hostName, userName, password)
		if self.DB.isConnectDB == True:
			self.rootWin = rootWin
			self.DBFrame()
		else:
			messagebox.showerror("Input Entry Error", "Please Enter correct login Entries")



	def getfoucs(self, event):

		try:
			cs = self.listDBs.curselection()  # list of items we were selected that store inside it variable called cs
			print(cs)
			self.dbvartxt.set(self.listDBs.get(cs[0])[0])
			print(self.listDBs.get(cs[0])[0])
		except IndexError:
			pass

	def createdb(self):
		print(self.dbvartxt.get())
		self.DB.createDB(self.dbvartxt.get())
		listofDBs = self.DB.shows("DATABASES")

		# fill rows of Available databases
		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)

	def useExistsDB(self):
		self.DB.database = self.dbvartxt.get()
		print(self.dbvartxt.get())
		self.DB.useOtherDB()
		self.tableFrame()

	def DBFrame(self):
		self.lableDBframe = tk.LabelFrame(self.rootWin, text="DataBase Entry", font=("Time Roman", 20, "bold"), bd=3, relief="ridge", bg="#73ebe1")

		# place where all available DB will show
		self.lableDBframe.grid(row=3, column=0, padx=10, pady=10)
		listFrame = tk.Frame(self.lableDBframe)
		listFrame.grid(row=1, column=0, columnspan=2, pady=10)
		avaiDBs = tk.Label(self.lableDBframe, text="Available DataBases  ", font=("Time Roman", 20, "bold"), fg="#6764fa")
		avaiDBs.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
		xscroll = tk.Scrollbar(listFrame, orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(listFrame, orient=tk.VERTICAL)
		self.listDBs= tk.Listbox(listFrame, fg="#000000", bd=0, relief="flat", font=("Time Roman", 15, "bold"))

		self.listDBs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=self.listDBs.xview)
		yscroll.config(command=self.listDBs.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)
		self.listDBs.pack(fill=tk.BOTH, side=tk.LEFT)

		self.dbvartxt = tk.StringVar()
		dbNameEntry = tk.Entry(self.lableDBframe, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, bg="red", fg="#ffffff", textvariable=self.dbvartxt)
		dbNameEntry.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
		useDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Use DB", command=self.useExistsDB).grid(row=3, column=0, padx=5, pady=5)
		createDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Create DB",  command=self.createdb).grid(row=3, column=1, padx=5, pady=5)

		# insert result to it's list boxes
		self.DB.database = self.dbvartxt.get()
		listofDBs = self.DB.shows("DATABASES")
		# fill rows of Available databases
		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)

		self.listDBs.bind("<<ListboxSelect>>", self.getfoucs)

		#self.tableFrame()

	def getfoucstable(self, event):
		try:
			cs = self.listTables.curselection()
			self.tablevar.set(self.listTables.get(cs[0])[0])
			print(self.listTables.get(cs[0])[0])
		except IndexError:
			pass

	def useExistsTable(self):
		# this method choosing while table will we use
		print("Tables is selecteed = ", self.tablevar.get())
		self.dbObjs = [] # list which contains DATABASE OBJECTS
		# new connection agian for new table because if user use new login info so new connection for that
		self.dbObjs.append(DBconnect.DB_connect(hostName=self.hostName, userName=self.userName, passsword=self.passwrd))
		self.dbObjs[-1].table = self.tablevar.get() # set table
		self.dbObjs[-1].database = self.dbvartxt.get() # set data base
		self.DB.table = self.tablevar.get()
		self.dbObjs[-1].useOtherDB()
		print("DB table selected = ", self.DB.table)
		self.nextWin = [] # store indiviual windows according to it
		self.nextWin.append(tk.Toplevel(self.rootWin))
		self.stdEXE = []  # student software object stores for indivisual database

		# =================== main Studented record software works ========================
		self.stdEXE.append(StudentManagementSystem(self.nextWin[-1], self.dbObjs[-1]))
		#========call
		self.stdEXE[-1].studRecordExe()

	def createTable(self):
		print(self.tablevar.get())
		self.DB.createtable(self.tablevar.get())
		self.listTables.delete(0, tk.END)
		listTables = self.DB.shows("TABLES")

		# fill rows of Available databases
		for table in listTables:
			self.listTables.insert(tk.END, table)

	def tableFrame(self):
		self.lableTableframe = tk.LabelFrame(self.rootWin, text="Tables Entry", font=("Time Roman", 20, "bold"), bd=3,
		                                  relief="ridge", bg="#73ebe1")

		# place where all available DB will show
		self.lableTableframe.grid(row=3, column=1, padx=10, pady=10)
		listFrame = tk.Frame(self.lableTableframe)
		listFrame.grid(row=1, column=0, columnspan=2, pady=10)
		avaiTables = tk.Label(self.lableTableframe, text="Available Tables  ", font=("Time Roman", 20, "bold"),
		                   fg="#6764fa")
		avaiTables.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
		xscroll = tk.Scrollbar(listFrame, orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(listFrame, orient=tk.VERTICAL)
		self.listTables = tk.Listbox(listFrame, fg="#000000", bd=0, relief="flat", font=("Time Roman", 15, "bold"))

		self.listTables.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=self.listTables.xview)
		yscroll.config(command=self.listTables.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)
		self.listTables.pack(fill=tk.BOTH, side=tk.LEFT)

		self.tablevar = tk.StringVar()
		tableNameEntry = tk.Entry(self.lableTableframe, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25,
		                       bg="red", textvariable=self.tablevar)
		tableNameEntry.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
		usetablebtn = tk.Button(self.lableTableframe, font=("Consolas", 15, "bold"), text="Use Table", command=self.useExistsTable).grid(row=3,
		                                                                                                 column=0,
                                                                                   padx=5, pady=5)
		createtablebtn = tk.Button(self.lableTableframe, font=("Consolas", 15, "bold"), text="Create Table", command=self.createTable).grid(row=3,
		                                                                                                       column=1,
		                                                                                                       padx=5,
		                                                                                                       pady=5)

		# insert result to it's list boxes
		Tables = self.DB.showTables()
		# fill rows of Available databases
		for table in Tables:
			self.listTables.insert(tk.END, table)

		self.listTables.bind("<<ListboxSelect>>", self.getfoucstable)


class GUI_project(ShowDBFrame):


	def __init__(self, RootWin):
		# toplevel window for connectivity to database
		super().__init__()  # Call the __init__ method of the parent class.
		self.RootWin = RootWin
		self.hostNameVar = tk.StringVar()
		self.userNameVar = tk.StringVar()
		self.passwordVar = tk.StringVar()


	def useInfo(self):

		#============= GUI frame which shows the DATABASE and Table INFO which are present on MYSQL DATABASE
		accessDB = ShowDBFrame()
		accessDB.InfoInput(self.topWin, self.hostNameVar.get(), self.userNameVar.get(), self.passwordVar.get())
		print(self.hostNameVar.get(), " : ", self.userNameVar.get(), " : ", self.passwordVar.get())

	def gui_db_connect(self):

		self.topWin = self.RootWin
		self.topWin.title("DataBase connectivity")

		hostLabel = tk.Label(self.topWin, text=" Host Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostLabel.grid(row=0, column=0, padx=5, pady=5)
		hostEntry = tk.Entry(self.topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.hostNameVar)
		hostEntry.grid(row=0, column=1, padx=5, pady=5)

		userNameLabel = tk.Label(self.topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		userNameLabel.grid(row=1, column=0, padx=5, pady=5)
		userEntry = tk.Entry(self.topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.userNameVar)
		userEntry.grid(row=1, column=1, padx=5, pady=5)

		passwdLabel = tk.Label(self.topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		passwdLabel.grid(row=2, column=0, padx=5, pady=5)
		userEntry = tk.Entry(self.topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.passwordVar, show="*")
		userEntry.grid(row=2, column=1, padx=5, pady=5)

		processBtn = tk.Button(self.topWin, text="GO", font= ("Consolas", 15, "bold"), bg="#5eff6c", fg="black", height=5, command=self.useInfo)
		processBtn.grid(row=0, column=3, rowspan=3)
