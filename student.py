from tkinter import *
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
		manageFrame.place(x=30, y=70, width=450, height=590)

		lbl_roll = Label(manageFrame, text="Roll No : ", font=("", 18, "bold"), fg="#adfc03", bg="#ff9933")
		lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")

		txt_roll = Entry(manageFrame, font=("Consolas", 15, "bold"), bd=2, relief="ridge", width=25)
		txt_roll.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		# ============== Record Showing Frame ================
				# This frame contain list box where  values will shows.
		recordFrame = LabelFrame(self.root, text="Showing Records", font=("Time Roman", 20, "bold"), bd=4, fg='Black', bg="#ff9933")
		recordFrame.place(x=500, y=70, width=800, height=590)

if __name__ == "__main__":
	win = Tk()
	root = StudentRecord(win)
	win.mainloop()