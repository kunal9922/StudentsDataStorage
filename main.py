from authentication import AuthenticWindow
import tkinter as tk

if __name__ == "__main__":
	# Create the main window
	win = tk.Tk()
	win.configure(bg="#73ebe1")
	# Set the icon
	win.iconbitmap(r'StudentDataStorage\Images\StudentDataStorageIcon.ico')
	gui = AuthenticWindow(win)
	gui.gui_db_connect()
	win.mainloop()