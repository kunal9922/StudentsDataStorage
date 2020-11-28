import tkinter as tk
import DBconnect
from tkinter import messagebox
class ShowDBFrame():
	def DBFrame(self, rootWin):
		self.lableDBframe = tk.LabelFrame(rootWin, text="DataBase Entry", font=("Time Roman", 20, "bold"), bd=4)

		# place where all available DB will show
		self.lableDBframe.grid(row=3, column=0, padx=10, pady=10)

		avaiDBs = tk.Label(self.lableDBframe, text="Available DataBases  ", font=("Time Roman", 20, "bold"), fg="#6764fa")
		avaiDBs.pack(side=tk.TOP, padx=10, pady=10)
		xscroll = tk.Scrollbar(self.lableDBframe, orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(self.lableDBframe, orient=tk.VERTICAL)
		self.listDBs= tk.Listbox(self.lableDBframe, fg="#000000", bd=0, relief="flat", font=("Time Roman", 20, "bold"))

		self.listDBs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=self.listDBs.xview)
		yscroll.config(command=self.listDBs.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)
		self.listDBs.pack()

		# insert result to it's list boxes
		self.DB = DBconnect.DB_connect("localhost", "root", "kunal9922soni", "studentRecordtest")
		listofDBs = self.DB.showDBs()

		for dbName in listofDBs:
			self.listDBs.insert(tk.END, dbName)


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
		hostLabel.grid(row=0, column=0, padx=20, pady=10)
		hostEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.hostNameVar)
		hostEntry.grid(row=0, column=1, padx=5, pady=10)

		userNameLabel = tk.Label(topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		userNameLabel.grid(row=1, column=0, padx=20, pady=10)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.userNameVar)
		userEntry.grid(row=1, column=1, padx=5, pady=10)

		passwdLabel = tk.Label(topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		passwdLabel.grid(row=2, column=0, padx=20, pady=10)
		userEntry = tk.Entry(topWin, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.passwordVar, show="*")
		userEntry.grid(row=2, column=1, padx=5, pady=10)

		#	hostName = tk.Label(topWin, text=" DB Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		#hostName.grid(row=3, column=0, padx=20, pady=10)

		ShowDBFrame.DBFrame(self, rootWin=topWin)


