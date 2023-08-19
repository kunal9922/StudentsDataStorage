from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class StudentManagementSystem:
	def __init__(self, root, DBObj):
		self.root = root
		self.root.config(bg="#f22245")
		# Set the icon
		self.root.iconbitmap(r'StudentDataStorage\Images\StudentDataStorageIcon.ico')
		title = Label(self.root, text="Student Management System", bd=5, relief="groove", font=("Cambria", 32, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
		self.root.title("Student Management System")
		# take the user monitor width and Height
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight = self.root.winfo_screenheight()

		self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')
		# before that of project will start so we take user id and password for database connectivity

		# DataBase connectivity
		self.DB = DBObj

	def studRecordExe(self):

		# ========== All variables which specifies the type of user input from input box from ManageFrame=======
		#Record Table Variables
		self.rollnum_var = IntVar()
		self.first_name_var = StringVar()
		self.last_name_var = StringVar()
		self.email_add_var = StringVar()
		
		# Basic Table Variables
		self.gender_var = StringVar()
		self.contact_var = StringVar()
		self.DOB_var = StringVar()
		self.txt_address_var = StringVar()
		self.searchBy = StringVar()
		self.searchTxt = StringVar()

		# =============== Manage Frame =================
				# This frame contain txt box where  values will insert
		manageFrame = LabelFrame(self.root, text="Manage Data", font=("Time Roman", 20, "bold"), bd=4, fg='Black', bg="#ff9933")
		manageFrame.place(x=30, y=70, width=460, height=600)
		# Create a Canvas inside the LabelFrame
		canvas = Canvas(manageFrame, bg="#ff9933", highlightthickness=0)
		canvas.pack(side="left", fill="both", expand=True)

		# Create a Scrollbar and attach it to the Canvas
		scrollbar = Scrollbar(manageFrame, orient="vertical", command=canvas.yview)
		scrollbar.pack(side="right", fill="y")

		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.bind("<Configure>", lambda event : canvas.configure(scrollregion=canvas.bbox("all")))

		 # Put your content inside the Canvas
		content_frame = Frame(canvas, bg="#ff9933")
		canvas.create_window((0, 0), window=content_frame, anchor="nw")

		lbl_roll = Label(content_frame, text="Roll No : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		txt_roll = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.rollnum_var)
		txt_roll.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		lbl_first_name = Label(content_frame, text="First Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_first_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		txt_first_name = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.first_name_var)
		txt_first_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		lbl_last_name = Label(content_frame, text="Last Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_last_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		txt_last_name = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.last_name_var)
		txt_last_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

		lbl_email = Label(content_frame, text="Email : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		txt_email = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.email_add_var)
		txt_email.grid(row=3, column=1, padx=10, pady=10, sticky="w")
		
		lbl_gender = Label(content_frame, text="Gender : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		com_gen = ttk.Combobox(content_frame, font=("Consolas", 18, "bold"), state="readonly", textvariable=self.gender_var)
		com_gen["values"] = ("Male", "Female", "Other")
		com_gen.grid(row=4, column=1, padx=10, pady=10)

		lbl_contact = Label(content_frame, text="Contact : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_contact.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		txt_contact = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.contact_var)
		txt_contact.grid(row=5, column=1, padx=10, pady=10, sticky="w")

		lbl_dob = Label(content_frame, text="D.O.B :", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_dob.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		txt_dob = Entry(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, textvariable=self.DOB_var)
		txt_dob.grid(row=6, column=1, padx=10, pady=10, sticky="w")

		lbl_address = Label(content_frame, text="Address : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_address.grid(row=7, column=0, padx=10, pady=10, sticky="w")
		self.txt_address = Text(content_frame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, height=5)
		self.txt_address.grid(row=7, column=1, padx=10, pady=10, sticky="w")

		#========== button frame ==========
		btnFrame = LabelFrame(canvas, bd=6, relief ="solid", fg='Black', bg="#7bfc03")
		btnFrame.place(x=10, y=500, width=420)

		self.addbtn = Button(btnFrame, text="Add", width=10, font=("Consolas", 10, "bold"), command=self.insert).grid(row=0,column=0, padx=10,pady=10)
		self.deletebtn = Button(btnFrame, text="Delete", width=10, font=("Consolas", 10, "bold"), command=self.deleteInfo).grid(row=0, column=1, padx=10, pady=10)
		self.updatebtn = Button(btnFrame, text="Update", width=10, font=("Consolas", 10, "bold"), command=self.updateData).grid(row=0, column=2, padx=10, pady=10)
		self.clearbtn = Button(btnFrame, text="Clear", width=10, font=("Consolas", 10, "bold"), command=self.clearData).grid(row=0, column=3, padx=10, pady=10)

		#================ showing information about UserName , DATABASE name,  Table Name==========
		DBInfoFrame= LabelFrame(self.root, relief="ridge", bg="#f22245")
		DBInfoFrame.place(x=30, y=680)
		usrNameTitle = Label(DBInfoFrame, text="User Name : ", font=("Consolas", 15, "bold"), bg="#f22245", fg="#ffffff")
		usrNameTitle.grid(row=0, column=0)
		usrnameLable = Label(DBInfoFrame, text=f"{self.DB.userName}, ", font=("Consolas", 15, "bold"), bg="#f22245",  fg="#ffffff")
		usrnameLable.grid(row=0, column=1)
		DBnameTitle = Label(DBInfoFrame, text="DataBase : ", font=("Consolas", 15, "bold"), bg="#f22245", fg="#ffffff")
		DBnameTitle.grid(row=0, column=2)
		DBnameLable = Label(DBInfoFrame, text=f"{self.DB.database}, ", font=("Consolas", 15, "bold"), bg="#f22245", fg="#ffffff")
		DBnameLable.grid(row=0, column=3)
		tablenameLable = Label(DBInfoFrame, text="Table : ", font=("Consolas", 15, "bold"), bg="#f22245", fg="#ffffff")
		tablenameLable.grid(row=0, column=4)
		tableNameLable = Label(DBInfoFrame, text=f"{self.DB.table}", font=("Consolas", 15, "bold"), bg="#f22245", fg="#ffffff")
		tableNameLable.grid(row=0, column=5)

		# ============== Record Showing Frame ================
				# This frame contain list box where  values will shows.
		recordFrame = LabelFrame(self.root, text="Showing Records", font=("Time Roman", 20, "bold"), bd=4 ,fg='Black', bg="#ff9933")
		recordFrame.place(x=500, y=70, width=830, height=600)

		searchLabel = Label(recordFrame, text="Search : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		searchLabel.grid(row=0, column=0, padx=10, pady=10)

		com_gen = ttk.Combobox(recordFrame, font=("Consolas", 18, "bold"), width=10, state="readonly", textvariable=self.searchBy)
		com_gen["values"] = ("RollNum", "First_Name", "Contact")
		com_gen.grid(row=0, column=1, padx=5, pady=10)

		txt_Search = Entry(recordFrame, font=("Consolas", 15, "bold"), bd=5, relief="ridge", width=25, textvariable=self.searchTxt)
		txt_Search.grid(row=0, column=2, padx=5, pady=10, sticky="w")

		searchBtn = Button(recordFrame, text="Search ", width=8, font=("Consolas", 14, "bold"), command=self.fetchBySearch).grid(row=0, column=3, padx=10, pady=10)
		showBtn = Button(recordFrame, text="ShowAll ", width=8, font=("Consolas", 14, "bold"), command=self.fetchData).grid(row=0, column=4, padx=10, pady=10)

		#=========== Table Data Frame ============
		tableFrame = Frame(recordFrame, bd=2, relief="ridge", bg="Crimson" )
		tableFrame.place(x=10, y=70, width=780, height=480)

		# ========== showing stored record on this frame ==========
		scroll_X = Scrollbar(tableFrame, orient=HORIZONTAL)
		scroll_Y = Scrollbar(tableFrame, orient=VERTICAL)
		self.studentRecordTable = ttk.Treeview(tableFrame, columns=("roll", "fname","lname", 
							      "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_X.set, yscrollcommand=scroll_Y.set)
		scroll_X.pack(side=BOTTOM, fill=X)
		scroll_Y.pack(side=RIGHT, fill=Y)
		scroll_X.config(command=self.studentRecordTable.xview)
		scroll_Y.config(command=self.studentRecordTable.yview)
		# Set anchor='center' for all columns using a loop
		for column in self.studentRecordTable['columns']:
			self.studentRecordTable.column(column, anchor='center') # Tree data comes in center 
		self.studentRecordTable.heading("roll", text="Roll No.")
		self.studentRecordTable.heading("fname", text="First Name")
		self.studentRecordTable.heading("lname", text="Last Name")
		self.studentRecordTable.heading("email", text="Email")
		self.studentRecordTable.heading("gender", text="Gender")
		self.studentRecordTable.heading("contact", text="Contact")
		self.studentRecordTable.heading("dob", text="Date Of Birth")
		self.studentRecordTable.heading("address", text="Address")
		self.studentRecordTable["show"] = "headings"
		self.studentRecordTable.pack(expand=True, fill=BOTH)

		#showing data
		self.fetchData()
		# get data from where the cursor will focus on
		self.studentRecordTable.bind("<ButtonRelease-1>", self.getCursorData)


	#====== DataBase operation functions =======
	def insert(self):
		# self.data = (self.rollnum_var.get(), self.first_name_var.get(), self.last_name_var.get(), 
		# 	        self.email_add_var.get(), self.gender_var.get(), self.contact_var.get(), self.DOB_var.get(), self.txt_address.get("1.0", END))
		self.data = [self.gender_var.get(), self.contact_var.get(), self.DOB_var.get(), self.txt_address.get("1.0", END),
	       self.rollnum_var.get(), self.first_name_var.get(), self.last_name_var.get(), self.email_add_var.get()]
		if self.rollnum_var.get() == '' or self.first_name_var.get() == '' :
			messagebox.showerror("RollNum or First Name not inserted", "insert RollNum and First Name field is mandatory")
		elif insertDone := self.DB.addIntoDB(self.data):
				if insertDone == 1:
					messagebox.showinfo("Insertion", "Insertion is successFully Done")
				elif insertDone == 2:
					messagebox.showerror("Insertion", f"Insertion is not possible because  Rollno {self.rollnum_var.get()} exist in table")
				else:
					messagebox.showerror("Insertion", 
			 			f'Database is unable to process please check the internet connection')
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
		self.rollnum_var.set("")
		self.first_name_var.set("")
		self.last_name_var.set("")
		self.email_add_var.set("")
		self.gender_var.set("")
		self.contact_var.set("")
		self.DOB_var.set("")
		self.txt_address.delete("1.0", END)

	def getCursorData(self, event):
		cursorFocusRow = self.studentRecordTable.focus()
		contents = self.studentRecordTable.item(cursorFocusRow)
		row = contents["values"]
		# show the values of where the cursor will hover on the studentRecordTable
		print(row)
		if len(row) != 0:
			self.rollnum_var.set(row[0])
			self.first_name_var.set(row[1])
			self.last_name_var.set(row[2])
			self.email_add_var.set(row[3])
			self.gender_var.set(row[4])
			self.contact_var.set(row[5])
			self.DOB_var.set(row[6])
			self.txt_address.delete("1.0", END)
			self.txt_address.insert("1.0", row[7])
		#print(row)

	def updateData(self):
		#'NewGender', 'NewContact', 'NewDOB', 'NewAddress', 101, 'NewFirstName', 'NewLastName', 'new_email@example.com', 101
		self.data = (self.gender_var.get(), self.contact_var.get(), self.DOB_var.get(), self.txt_address.get("1.0", END), self.rollnum_var.get(), self.first_name_var.get(), self.last_name_var.get(), self.email_add_var.get(), self.rollnum_var.get())

		self.DB.updateData(self.data)
		# when any update happen so update our treeView
		self.fetchData()
		# And clear our text box for again put new data
		self.clearData()

	def deleteInfo(self):
		try:
			keyRollNum = self.rollnum_var.get()
			self.DB.deleteData(key=keyRollNum)
		except Exception:
			messagebox.showerror("Roll Number Field", "Please Enter Roll Number")
		# when any update happen so update our treeView
		self.fetchData()
		# And clear our text box for again put new data
		self.clearData()

	def fetchBySearch(self):
		if self.searchBy.get() == "":
			messagebox.showerror("Errror", "choose any field on search box")
		elif self.searchTxt.get() == "":
			messagebox.showerror("Error", "Insert into text field. which you want to search")
		else:
			rows = self.DB.searchByFetch(self.searchBy.get(), self.searchTxt.get())
			if len(rows) != 0:  # data is update in a table so we need to show new data that's why we delete data in a treeView
				self.studentRecordTable.delete(*self.studentRecordTable.get_children())
				# updatation
				for row in rows:
					self.studentRecordTable.insert('', END, values=row)
