from tkinter import *
from tkinter import ttk
import mysql.connector

class StudentRecord:
	def __init__(self, root):
		self.root = root
		title = Label(self.root, text="Student Management System", bd=5, relief="groove", font=("Cambria", 32, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
		self.root.title("Student Management System")
		# take the user monitor width and Height
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight = self.root.winfo_screenheight()

		self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')

		# =============== Manage Frame =================
				# This frame contain txt box where  values will insert
		manageFrame = LabelFrame(self.root, text="Mange Data", font=("Time Roman",20,"bold"), bd=4, fg='Black', bg="#ff9933")
		manageFrame.place(x=30, y=70, width=460, height=550)

		lbl_roll = Label(manageFrame, text="Roll No : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		txt_roll = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_roll.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		lbl_Name = Label(manageFrame, text="Name : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		txt_Name = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		lbl_Sem = Label(manageFrame, text="Semester : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Sem.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		txt_Sem = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Sem.grid(row=2, column=1, padx=10, pady=10, sticky="w")

		lbl_Email = Label(manageFrame, text="Email : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_Email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		txt_Email = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_Email.grid(row=3, column=1, padx=10, pady=10, sticky="w")

		lbl_address = Label(manageFrame, text="Address : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		txt_address = Text(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25, height=5)
		txt_address.grid(row=4, column=1, padx=10, pady=10, sticky="w")

		lbl_gender = Label(manageFrame, text="Gender : ", font=("Consolas", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_gender.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		com_gen = ttk.Combobox(manageFrame, font=("Consolas", 18, "bold"))
		com_gen["values"] = ("Male", "Female", "Other")
		com_gen.grid(row=5, column=1, padx=10, pady=10)

		lbl_dob = Label(manageFrame, text="D.O.B :", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_dob.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		txt_dob = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_dob.grid(row=6, column=1, padx=10, pady=10, sticky="w")

		# ============== Record Showing Frame ================
				# This frame contain list box where  values will shows.
		recordFrame = LabelFrame(self.root, text="Showing Records", font=("Time Roman", 20, "bold"), bd=4, fg='Black', bg="#ff9933")
		recordFrame.place(x=500, y=70, width=800, height=550)

if __name__ == "__main__":
	win = Tk()
	root = StudentRecord(win)
	win.mainloop()