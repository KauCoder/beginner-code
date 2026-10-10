import time
import pyautogui
import keyboard  # You can install this via: pip install keyboard

# --- Configuration ---
TOGGLE_KEY = 'ctrl+g'  # Press Ctrl + G to start or pause the autoclicker
EXIT_KEY = 'ctrl+q'    # Press Ctrl + Q to completely close the script
CLICK_DELAY = 0.01     # Time between clicks in seconds (0.01 = 100 clicks/sec)

print(f"--- PyAutoGUI Autoclicker Active ---")
print(f"Press [{TOGGLE_KEY.upper()}] to Start / Pause")
print(f"Press [{EXIT_KEY.upper()}] to Quit completely")

clicking = False

while True:
    # Check if user wants to toggle the clicking state
    if keyboard.is_pressed(TOGGLE_KEY):
        clicking = not clicking
        state = "STARTED" if clicking else "PAUSED"
        print(f"Autoclicker {state}")
        time.sleep(0.3)  # Brief pause to prevent accidental double-toggles

    # Check if user wants to kill the program
    if keyboard.is_pressed(EXIT_KEY):
        print("Exiting Autoclicker...")
        break

    # If active, perform the click
    if clicking:
        pyautogui.click()
        time.sleep(CLICK_DELAY)