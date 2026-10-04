import tkinter as tk
import random

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.range_max = 100
        self.max_attempts = 10
        self.reset_game()

        # Title/instructions label
        self.label = tk.Label(master, text=f"Guess a number between 1 and {self.range_max}")
        self.label.pack(pady=10)

        # Entry box for guesses
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        # Feedback label
        self.feedback = tk.Label(master, text="")
        self.feedback.pack(pady=5)

        # Play again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state="disabled")

    def reset_game(self):
        self.random_number = random.randint(1, self.range_max)
        self.attempts_left = self.max_attempts
        if hasattr(self, "feedback"):
            self.feedback.config(text="")
        if hasattr(self, "entry"):
            self.entry.delete(0, tk.END)
        if hasattr(self, "submit_button"):
            self.submit_button.config(state="normal")
        if hasattr(self, "play_again_button"):
            self.play_again_button.config(state="disabled")

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="Please enter a valid number.")
            return

        guess = int(guess)

        if not (1 <= guess <= self.range_max):
            self.feedback.config(text=f"Out of range! Enter between 1 and {self.range_max}.")
            return

        self.attempts_left -= 1

        if guess < self.random_number:
            self.feedback.config(text="Too low!")
        elif guess > self.random_number:
            self.feedback.config(text="Too high!")
        else:
            self.feedback.config(text=f"Correct! The number was {self.random_number}.")
            self.end_game()
            return

        if self.attempts_left == 0:
            self.feedback.config(text=f"Out of attempts! The number was {self.random_number}.")
            self.end_game()

    def end_game(self):
        self.submit_button.config(state="disabled")
        self.play_again_button.config(state="normal")

# Create and run the GUI app
root = tk.Tk()

screen_width = root.winfo_width()
screen_height = root.winfo_height()

screen = root

game = GuessingGameGUI(root)
root.mainloop()
