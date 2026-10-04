import tkinter as tk
from tkinter import font

root = tk.Tk()
title = root.title("Hello!!!")
main_font = font.Font(family="Times New Roman", weight="normal", size=15)

text = tk.Label(root, text="Hello there!", font=(main_font))
text.pack()

root.mainloop()