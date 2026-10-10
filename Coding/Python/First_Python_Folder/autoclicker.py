import time
import pyautogui
from pynput import keyboard

# --- OPTIMIZED MAX SPEED CONFIGURATION ---
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.0  

clicking = False
running = True

# Track the state of the Control key
ctrl_pressed = False

# Safe burst settings to prevent Mac event queue lockup
BURST_COUNT = 25       
QUEUE_BUFFER = 0.005   

print("--- Ctrl+G Autoclicker Active ---")
print("Press [Ctrl + G] to Start / Pause")
print("Press [Ctrl + Q] to Quit completely")
print("EMERGENCY: Slam mouse into the TOP-LEFT corner to trigger Fail-Safe.")

def on_press(key):
    global clicking, running, ctrl_pressed
    
    # Check if a modifier key was pressed
    if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = True
        return

    try:
        # Only trigger if Control is actively being held down
        if ctrl_pressed:
            if key.char == 'g':
                clicking = not clicking
                print(f"Autoclicker: {'RUNNING' if clicking else 'PAUSED'}")
            elif key.char == 'q':
                print("Exiting...")
                running = False
                return False
    except AttributeError:
        pass

def on_release(key):
    global ctrl_pressed
    # Track when the user lets go of the Control key
    if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False

# Start listening for both presses and releases
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Main execution loop
while running:
    if clicking:
        pyautogui.click(clicks=BURST_COUNT, interval=0.0001)
        time.sleep(QUEUE_BUFFER)
    else:
        time.sleep(0.1)