import random

choices = ["yes", "no"]

def roll():
    choice = random.choice(choices)
    return choice

def main():
    play = input("Do you want to roll the yes-no (eraser) (y/n)?")

    if play.lower() == "y":
        print(roll())
    else:
        print("Have a nice day!")
        quit()

while True:
    main()