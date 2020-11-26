import tkinter as tk
from tkinter import messagebox
class ShowDBFrame():
	def DBFrame(self, rootWin):
		self.lableDBframe = tk.LabelFrame(rootWin, text="DataBase Entry", font=("Time Roman", 20, "bold"), bd=4,width=400, height=200)
		'''dblabel = tk.Label(self.lableDBframe, text="Have DATABASE ?")
		dbHave = tk.Checkbutton(rootWin, text="Yes", onvalue=1, offvalue=0)
		dbHaveNot = tk.Checkbutton(rootWin, text="No", onvalue=1, offvalue=0)
		'''
		# place where all available DB will show
		self.lableDBframe.grid(row=3, column=0, padx=10, pady=10)
		xscroll = tk.Scrollbar(self.lableDBframe,orient=tk.HORIZONTAL)
		yscroll = tk.Scrollbar(self.lableDBframe, orient=tk.VERTICAL)
		listDBs= tk.Listbox(self.lableDBframe, bg="#22e6d5", fg="#000000", bd=2, relief="ridge", font=("Time Roman", 20, "bold"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

		xscroll.pack(fill=tk.X, side=tk.BOTTOM)
		xscroll.config(command=listDBs.xview)
		yscroll.config(command=listDBs.yview)
		yscroll.pack(fill=tk.Y, side=tk.RIGHT)

		listDBs.pack()

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


