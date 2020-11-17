from tkinter import *
from tkinter import ttk
import DBconnect

class StudentManagementSystem:
	def __init__(self, root):
		self.root = root
		title = Label(self.root, text="Student Management System", bd=5, relief="groove", font=("Cambria", 32, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
		self.root.title("Student Management System")
		# take the user monitor width and Height
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight = self.root.winfo_screenheight()

		self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')
		# DataBase connectivity
		self.DB = DBconnect.DB_connect()
		self.studRecordExe()

	def studRecordExe(self):

		# ========== All variables which specifies the type of user input from input box from ManageFrame=======
		self.RollNum_var = IntVar()
		self.Name_var = StringVar()
		self.contact_var = StringVar()
		self.EmailAdd_var = StringVar()
		self.Gender_var = StringVar()
		self.DOB_var = StringVar()

		# =============== Manage Frame =================
				# This frame contain txt box where  values will insert
		manageFrame = LabelFrame(self.root, text="Manage Data", font=("Time Roman", 20, "bold"), bd=4, fg='Black', bg="#ff9933")
		manageFrame.place(x=30, y=70, width=460, height=600)

		lbl_roll = Label(manageFrame, text="Roll No : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		txt_roll = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.RollNum_var)
		txt_roll.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		lbl_Name = Label(manageFrame, text="Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		txt_Name = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.Name_var)
		txt_Name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		lbl_Contact = Label(manageFrame, text="Contact : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Contact.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		txt_Contact = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.contact_var)
		txt_Contact.grid(row=2, column=1, padx=10, pady=10, sticky="w")

		lbl_Email = Label(manageFrame, text="Email : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		txt_Email = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.EmailAdd_var)
		txt_Email.grid(row=3, column=1, padx=10, pady=10, sticky="w")

		lbl_gender = Label(manageFrame, text="Gender : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		com_gen = ttk.Combobox(manageFrame, font=("Consolas", 18, "bold"), state="readonly", textvariable=self.Gender_var)
		com_gen["values"] = ("Male", "Female", "Other")
		com_gen.grid(row=4, column=1, padx=10, pady=10)

		lbl_dob = Label(manageFrame, text="D.O.B :", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_dob.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		txt_dob = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.DOB_var)
		txt_dob.grid(row=5, column=1, padx=10, pady=10, sticky="w")

		lbl_address = Label(manageFrame, text="Address : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_address.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		self.txt_address = Text(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, height=5)
		self.txt_address.grid(row=6, column=1, padx=10, pady=10, sticky="w")

		#========== button frame ==========
		btnFrame = LabelFrame(manageFrame, bd=6, relief ="solid", fg='Black', bg="#7bfc03")
		btnFrame.place(x=10, y=500, width=430)

		self.addbtn = Button(btnFrame, text="Add", width=10, font=("Consolas", 10, "bold"), command=self.insert).grid(row=0,column=0, padx=10,pady=10)
		self.deletebtn = Button(btnFrame, text="Delete", width=10, font=("Consolas", 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
		self.updatebtn = Button(btnFrame, text="Update", width=10, font=("Consolas", 10, "bold")).grid(row=0, column=2, padx=10, pady=10)
		self.clearbtn = Button(btnFrame, text="Clear", width=10, font=("Consolas", 10, "bold"), command=self.clearData).grid(row=0, column=3, padx=10, pady=10)


		# ============== Record Showing Frame ================
				# This frame contain list box where  values will shows.
		recordFrame = LabelFrame(self.root, text="Showing Records", font=("Time Roman", 20, "bold"), bd=4 ,fg='Black', bg="#ff9933")
		recordFrame.place(x=500, y=70, width=830, height=600)

		searchLabel = Label(recordFrame, text="Search : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		searchLabel.grid(row=0, column=0, padx=10, pady=10)

		com_gen = ttk.Combobox(recordFrame, font=("Consolas", 18, "bold"), width=10, state="readonly")
		com_gen["values"] = ("Roll Num", "Name", "Contact", "Email", "Gender", "DateOfBirth", "Address")
		com_gen.grid(row=0, column=1, padx=5, pady=10)

		txt_Search = Entry(recordFrame, font=("Consolas", 15, "bold"), bd=5, relief="ridge", width=25)
		txt_Search.grid(row=0, column=2, padx=5, pady=10, sticky="w")

		searchBtn = Button(recordFrame, text="Search ", width=8, font=("Consolas", 14, "bold")).grid(row=0, column=3, padx=10, pady=10)
		showBtn = Button(recordFrame, text="ShowAll ", width=8, font=("Consolas", 14, "bold")).grid(row=0, column=4, padx=10, pady=10)

		#=========== Table Data Frame ============
		tableFrame = Frame(recordFrame, bd=2, relief="ridge", bg="Crimson" )
		tableFrame.place(x=10, y=70, width=780, height=480)

		# ========== showing stored record on this frame ==========
		scroll_X = Scrollbar(tableFrame, orient=HORIZONTAL)
		scroll_Y = Scrollbar(tableFrame, orient=VERTICAL)
		self.studentRecordTable = ttk.Treeview(tableFrame, columns=("roll", "name", "contact", "email", "gender", "dob", "address"), xscrollcommand=scroll_X.set, yscrollcommand=scroll_Y.set)
		scroll_X.pack(side=BOTTOM, fill=X)
		scroll_Y.pack(side=RIGHT, fill=Y)
		scroll_X.config(command=self.studentRecordTable.xview)
		scroll_Y.config(command=self.studentRecordTable.yview)
		self.studentRecordTable.heading("roll", text="Roll Num")
		self.studentRecordTable.heading("name", text="Name")
		self.studentRecordTable.heading("contact", text="Contact")
		self.studentRecordTable.heading("email", text="Email")
		self.studentRecordTable.heading("gender", text="Gender")
		self.studentRecordTable.heading("dob", text="DateOFBirth")
		self.studentRecordTable.heading("address", text="Address")
		self.studentRecordTable["show"] = "headings"
		self.studentRecordTable.pack(expand=True, fill=BOTH)

		#showing data
		self.fetchData()
		# get data from where the cursor will focus on
		self.studentRecordTable.bind("<ButtonRelease-1>", self.getCursorData)


	#====== DataBase operation functions =======
	def insert(self):
		data = (self.RollNum_var.get(), self.Name_var.get(), self.contact_var.get(),
			        self.EmailAdd_var.get(), self.Gender_var.get(), self.DOB_var.get(), self.txt_address.get("1.0", END))
		self.DB.addIntoDB(data)
		# when any insertion happen so update our treeView
		self.fetchData()

	def fetchData(self):
		rows = self.DB.gettingData()
		if len(rows) != 0:  # data is update in a table so we need to show new data that's why we delete data in a treeView
			self.studentRecordTable.delete(*self.studentRecordTable.get_children())
			# updatation
			for row in rows:
				self.studentRecordTable.insert('', END, values=row)

	def clearData(self):
		self.RollNum_var.set("")
		self.Name_var.set("")
		self.contact_var.set("")
		self.EmailAdd_var.set("")
		self.Gender_var.set("")
		self.DOB_var.set("")
		self.txt_address.delete("1.0", END)

	def getCursorData(self, event):
		cursorFocusRow = self.studentRecordTable.focus()
		contents = self.studentRecordTable.item(cursorFocusRow)
		row = contents["values"]
		# show the values of where the cursor will hover on the studentRecordTable
		self.RollNum_var.set(row[0])
		self.Name_var.set(row[1])
		self.contact_var.set(row[2])
		self.EmailAdd_var.set(row[3])
		self.Gender_var.set(row[4])
		self.DOB_var.set(row[5])
		self.txt_address.delete("1.0", END)
		self.txt_address.insert("1.0", row[6])

		#print(row)

if __name__ == "__main__":
	win = Tk()
	root = StudentManagementSystem(win)
	win.mainloop()