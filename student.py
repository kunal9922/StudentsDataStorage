from tkinter import *
import mysql.connector

class StudentRecord:
	def __init__(self, root):
		self.root = root
		title = Label(self.root, text="Student Management System", bd=5,relief="groove",font=("Cambria",32,"bold"),bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)
		self.root.title("Student Management System")
		# take the user monitor width and Height
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight = self.root.winfo_screenheight()

		self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')

if __name__ == "__main__":
	win = Tk()
	root = StudentRecord(win)
	win.mainloop()