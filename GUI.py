import tkinter as tk
import DBconnect
from tkinter import messagebox
class ShowDBFrame():
	def DBFrame(self, rootWin):
		self.lableDBframe = tk.LabelFrame(rootWin, text="DataBase Entry", font=("Time Roman", 20, "bold"), bd=3, relief="ridge", bg="#73ebe1")

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

		# insert result to it's list boxes
		self.DB = DBconnect.DB_connect("localhost", "root", "kunal9922soni", "studentRecordtest")
		listofDBs = self.DB.showDBs()

		#fill rows of Available databases
		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)

		self.dbvar = tk.StringVar()
		dbNameEntry = tk.Entry(self.lableDBframe, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25,bg="red", textvariable=self.dbvar)
		dbNameEntry.grid(row=2,column=0, padx=5,pady=5, columnspan=2)
		useDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Use DB").grid(row=3, column=0, padx=5, pady=5)
		createDBbtn = tk.Button(self.lableDBframe, font=("Consolas", 15, "bold"), text="Create DB").grid(row=3, column=1, padx=5, pady=5)


class GUI_project(ShowDBFrame):
	def __init__(self, RootWin):
		# toplevel window for connectivity to database
		self.RootWin = RootWin

	def gui_db_connect(self):

		self.hostNameVar = tk.StringVar()
		self.userNameVar = tk.StringVar()
		self.passwordVar = tk.StringVar()

		topWin = tk.Toplevel(self.RootWin, bg="#73ebe1", bd=5)
		topWin.title("DataBase connectivity")

		hostLabel = tk.Label(topWin, text=" Host Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostLabel.grid(row=0, column=0, padx=20, pady=5)
		hostEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.hostNameVar)
		hostEntry.grid(row=0, column=1, padx=5, pady=5)

		userNameLabel = tk.Label(topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		userNameLabel.grid(row=1, column=0, padx=20, pady=5)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.userNameVar)
		userEntry.grid(row=1, column=1, padx=5, pady=5)

		passwdLabel = tk.Label(topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		passwdLabel.grid(row=2, column=0, padx=20, pady=5)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.passwordVar, show="*")
		userEntry.grid(row=2, column=1, padx=5, pady=5)

		#	hostName = tk.Label(topWin, text=" DB Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		#hostName.grid(row=3, column=0, padx=20, pady=10)

		ShowDBFrame.DBFrame(self, rootWin=topWin)


