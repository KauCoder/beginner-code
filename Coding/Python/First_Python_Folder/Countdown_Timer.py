import time

def countdown(total_seconds):
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        duration_input = int(input("Enter the countdown duration in seconds: "))
        if duration_input > 0:
            countdown(duration_input)
        else:
            print("Please enter a positive number of seconds.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
