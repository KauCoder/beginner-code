import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
title = root.title("My first Tkinter app!!!")


title_font = font.Font(family="Times New Roman", size=45, weight="bold", underline=True)
heading_font = font.Font(family="Calibri", size=30, weight="normal")
text_font = font.Font(family="Calibri", size=20, weight="normal")

class Paragraph:
    def __init__(self, heading: str, text: str, font: font.Font):
        self.heading = heading
        self.text = text
        self.font = font
        heading.capitalize()
        text.capitalize()

# Set the window size
width = 600
height = 500

# Get the screen width and height
screen_width = root.winfo_screenwidth()   # Screen width
screen_height = root.winfo_screenheight() # Screen height

# Calculate the position to center the window
position_top = int(screen_height / 2 - height / 2)
position_left = int(screen_width / 2 - width / 2)

# Set the window size and position (centered)
root.geometry(f"{width}x{height}+500+100")

# Create a Title
label = tk.Label(root, text="Hello Tkinter!!!", font=(title_font))
label.pack()

# Create the text
text = tk.Label(root, text="\n\nI hope you like this, I have been updating this for a couple of days.\nI am planning on learning other GUI modules in Python!!!")
text.pack()

# Create the text
text = Paragraph(heading="This is my first Tkinter app!!!", text=f"{text}", font=text_font)


# Start the app
root.mainloop()