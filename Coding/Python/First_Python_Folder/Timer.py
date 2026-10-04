import time

def countdown():
    Countdown_Time = (input("Enter the number to count down from: "))
    while Countdown_Time.isdigit() == False or int(Countdown_Time) <= 0:
        print("Please enter a valid number greater than 0.")
        Countdown_Time = input("Enter the number to count down from: ")
    for i in range(int(Countdown_Time), 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!!!")

countdown()
while True:
    do_again = input("Do you want to set another timer? (yes/no): ").strip().lower()
    if do_again == "no":
        print("Goodbye!")
        break
    elif do_again == "yes":
        countdown()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue