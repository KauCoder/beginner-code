import tkinter as tk

text1 = "Hi, this is a fancy lettering example! "
text2 = "This looks like I am typing it in real-time, But I am not!"

def type_text(label, text, idx=0, next_text=None):
    if idx < len(text):
        label.config(text=label.cget("text") + text[idx])
        label.after(50, type_text, label, text, idx+1, next_text)
    elif next_text:
        label.after(1500, lambda: [label.config(text=""), type_text(label, next_text)]) 

root = tk.Tk()
root.title("Typing Effect")

# Set window size
window_width = 500
window_height = 500

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(expand=True, fill="both")

type_text(label, text1, next_text=text2)

root.mainloop()