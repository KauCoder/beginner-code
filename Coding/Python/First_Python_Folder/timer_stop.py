import time
import threading

goal = 5  # seconds
running = True

def wait_for_enter():
    global running
    input()  # This waits silently for the user to press Enter
    running = False

def main():
    global running
    running = True # Reset the running flag for each new try

    print(f"Your goal is {goal} seconds.")
    input("Press Enter to start the timer...")

    # Record the exact moment the timer starts
    start_time = time.time()

    # Start a background thread that listens for the second Enter press
    input_thread = threading.Thread(target=wait_for_enter)
    input_thread.start()

    # Keep updating the display while the thread is waiting for Enter
    while running:
        # Calculate exactly how much time has passed since start_time
        time_elapsed = time.time() - start_time
        print(f"{time_elapsed:.3f}", flush=True, end="\r")

    # Final calculations once Enter is pressed
    final_time = time.time() - start_time
    difference = abs(final_time - goal)

    print(f"You were off by: {difference:.3f}")

if __name__ == "__main__":
    main()
    retry = input("Do you want to try again? (press 'enter' for yes) or type 'n' then 'enter' for no): ")
    if retry.lower() == 'n':
        print("Bye! Thanks for playing!")
    else:
        main()