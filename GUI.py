import tkinter as tk
from tkinter import messagebox

class GUI_project():
	def __init__(self, RootWin):
		# toplevel window for connectivity to database
		self.RootWin = RootWin

	def gui_db_connect(self):
		topWin = tk.Toplevel(self.RootWin, bg="#73ebe1", bd=5)
		topWin.title("DataBase connectivity")

		hostName = tk.Label(topWin, text=" Host Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostName.grid(row=0, column=0, padx=20, pady=10)

		hostName = tk.Label(topWin, text=" User Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostName.grid(row=1, column=0, padx=20, pady=10)

		hostName = tk.Label(topWin, text=" PassWord : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostName.grid(row=2, column=0, padx=20, pady=10)

		hostName = tk.Label(topWin, text=" DB Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		hostName.grid(row=3, column=0, padx=20, pady=10)

