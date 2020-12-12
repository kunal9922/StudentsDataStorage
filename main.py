from GUI import GUI_project
import tkinter as tk
from student import  StudentManagementSystem
if __name__ == "__main__":
	win = tk.Tk()
	win.configure(bg="#73ebe1")
	gui = GUI_project(win)
	gui.gui_db_connect()
	win.mainloop()