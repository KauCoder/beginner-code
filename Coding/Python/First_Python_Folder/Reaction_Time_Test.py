import time
import random

input("Press 'enter' when the screen says 'NOW!' to test your reaction time. Press enter once right now to continue: ")

def reaction_time_test():

    time.sleep(random.randint(2, 5))

    start_time = time.time()
    input("NOW!")
    end_time = time.time()

    reaction_time = end_time - start_time
    reaction_time = reaction_time * 1000
    if round(reaction_time, 0) == 0:
        print("\nYou pressed enter too early! Try again.")
    print(f"Your reaction time is: {reaction_time:.0f}ms.")

if __name__ == "__main__":
    while True:
        reaction_time_test()
        play_again = input("Wanna play again? (enter) Type 'n' then enter to quit: ")
        if play_again.lower() == 'n':
            print("Thanks for playing! Goodbye!")
            break