import tkinter as tk
from tkinter import messagebox
import pypy12
def proceed():
    result = messagebox.askyesno("Confirmation", "Do you want to proceed?")
    if result:
        print("Proceeding...")
        # Call your specific function here
        pypy12.generateCode()
        messagebox.showinfo("Success", "Booked Successfully")
        root = tk.Tk()
        root.withdraw()

    else:
        print("Cancelled.")
    root = tk.Tk()
    root.withdraw()

