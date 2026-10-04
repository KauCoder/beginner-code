import random
import time

words = ["hangman", "wonder", "imaginary", "python", "programming"]

while True:
    word = random.choice(words)
    tries_left = 5

    print("\nNew word selected!\n")

    while tries_left > 0:
        guess = input(f"Guess a letter/word (Tries left: {tries_left}): ").lower()

        if len(guess) > 1:
            if guess == word:
                print("YOU WON!!!")
                break
            else:
                print("Wrong word!")
                tries_left -= 1

        elif len(guess) == 1:
            if guess in word:
                print("Yes, that letter is in the word!")
            else:
                print("Nope!")
                tries_left -= 1

        time.sleep(0.5)

    if tries_left == 0:
        print(f"You lost! The word was \"{word}\"")

    retry = input("Do you want to try again (y/n): ").lower()
    if retry != "y":
        break

time.sleep(0.5)
print("THANK YOU FOR PLAYING!!!")