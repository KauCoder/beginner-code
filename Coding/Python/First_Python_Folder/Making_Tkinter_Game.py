import tkinter as tk
from tkinter import font

root = tk.Tk()

# Fullscreen setup
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Fonts
Title_Font = font.Font(family="Times New Roman", size=50, weight="bold")
button_font = font.Font(family="Verdana", size=30, weight="normal")

# Title and label
root.title("Press a button")
label = tk.Label(root, text="Press the button below!!!", font=Title_Font)
label.pack(padx=30, pady=30)

# Function to update label
def say_hello():
    message_label.config(text="Hello!!!")

# 🔥 Real custom "press" simulation
def press_button_effect(event=None):
    # Change button to look pressed
    button.config(relief="sunken", bg="#45a049")
    root.update_idletasks()

    # Call the function
    say_hello()

    # After short delay, reset to normal look
    root.after(150, lambda: button.config(relief="raised", bg="#4CAF50"))

# Create the button
button = tk.Button(
    root,
    text="Click Me!!!",
    font=button_font,
    padx=20,
    pady=20,
    relief="raised",
    bd=5,
    bg="#4CAF50",
    fg="black",
    activebackground="#45a049",
    activeforeground="black",
    command=say_hello  # For mouse click
)
button.pack()

# Focus the button so Enter works
button.focus_set()

# Bind Enter key to simulate full visual + logic click
button.bind("<Return>", press_button_effect)

# Message label
message_label = tk.Label(root, text="", font=button_font)
message_label.pack(pady=10)

root.mainloop()

