import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x300")
root.title("SIL - Software Installment Labs")
root.size = root.maxsize()
button = tk.Button(root, text="Introduction", command=lambda: messagebox.showinfo("Info", "Welcome To Software Installment Labs"))
button.pack()
root.mainloop()
if button:
    messagebox.askyesno("Question", "Install net-virus.com?")
    if messagebox.askyesno("Question"):
        messagebox.showinfo("ResponseTrue", "<@python.messageAlert('net-virus.exe ')> downloaded!")
    else:
        messagebox.showinfo("ResponseFalse", "<@python.link(net-virus.exe).#!FORCE_DOWNLOAD!>")