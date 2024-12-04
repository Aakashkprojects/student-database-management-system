import tkinter as tk
from gui import StudentManagementSystem

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()