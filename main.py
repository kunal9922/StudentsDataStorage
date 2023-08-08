from authentication import AuthenticWindow
from tkinter import Tk
def main():
	# Create the main window
    win = Tk()
    win.configure(background="#73ebe1")
    # Set the icon
    win.iconbitmap(r'StudentDataStorage\Images\StudentDataStorageIcon.ico')
    gui = AuthenticWindow(win)
    gui.gui_db_connect()
    win.mainloop()

if __name__ == "__main__":
	main()