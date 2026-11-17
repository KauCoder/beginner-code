import time
import threading
import sys

goal = 5  
running = True

def wait_for_enter():
    global running
    input()  
    running = False

def flush_input():
    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except ImportError:
        pass

def main():
    global running 
    running = True 
    
    flush_input()
    
    print(f"\nYour goal is {goal} seconds.")
    input("Press Enter to start the timer...")

    start_time = time.time()

    flush_input()

    input_thread = threading.Thread(target=wait_for_enter)
    input_thread.start()

    while running:
        time_elapsed = time.time() - start_time
        print(f"{time_elapsed:.3f}", flush=True, end="\r")

    final_time = time.time() - start_time
    difference = abs(final_time - goal)

    print(f"\nYou were off by: {difference:.3f}")

if __name__ == "__main__":
    while True:
        main()
        retry = input("Do you want to try again? (press 'enter' for yes) or type 'n' then 'enter' for no): ")
        if retry.lower() == 'n':
            print("Bye! Thanks for playing!")
            break