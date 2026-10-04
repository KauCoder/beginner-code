# Built in imports
import os
import time
import random
import sys
import subprocess

# My imports
import extension_os_say
import App_Opener

# Functions
def printwl(msg="", /, *, flush=False):
    """Prints a message to the console. No sep supported."""
    print(msg, flush=flush)
def kill():
    os.abort()
def say_ext(txt):
    """An extension of the standard OS 'say' command, as now you can say super long words without it sounding weird."""
    extension_os_say.say(txt)
def openApp(App, /):
    """Opens any Macbook desktop application. Only works on Mac."""
    App_Opener(App)
def script_type(msg, /, *, delay=0.5, speed=0.1):
    """
    Outputs a message to a console one character at a time, thus giving the text a 'typing' feel. flush, sep, and end are not supported.
    Can potentially be used for 'scripting' (don't actually script with this)
    """
    time.sleep(delay)
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    return msg

def script_type_real(test, speed=0.1, delay=0.5):
    # Wait the initial delay before starting
    time.sleep(delay)
    
    typed_text = ""
    
    for char in test:
        # 1. Print the character instantly to the screen
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # 2. Track the character
        typed_text += char
        
        # 3. Calculate human-like variance
        # Creates a random speed float around your base speed (e.g., between 0.05 and 0.15)
        base_variance = random.uniform(speed * 0.5, speed * 1.5)
        
        # 4. Add extra micro-pauses for natural typing flow
        if char == " ":
            # Humans pause slightly at the end of words
            time.sleep(base_variance + 0.05)
        elif char in [".", ",", "!", "?"]:
            # Humans pause longer at punctuation
            time.sleep(base_variance + 0.15)
        else:
            # Standard keystroke
            time.sleep(base_variance)
            
    return typed_text

def script_type_virtual(text, speed=0):
    # ⏱️ CHANGE THIS SINGULAR VARIABLE ONLY (In seconds per letter)
    # 0.005 = Blazing Fast | 0.02 = Snappy Machine | 0.05 = Relaxed Robot
    SECONDS_PER_LETTER = 0.02
    
    # Escape any tricky characters for AppleScript syntax safety
    escaped_text = text.replace('\\', '\\\\').replace('"', '\\"')
    
    # Build a single native macOS command that runs the loop inside the OS itself
    applescript = (
        'tell application "System Events"\n'
        f'    set txt to "{escaped_text}"\n'
        '    repeat with i from 1 to count of characters in txt\n'
        '        keystroke (character i of txt)\n'
        f'        delay {SECONDS_PER_LETTER}\n' # Uses your single variable directly
        '    end repeat\n'
        'end tell'
    )
    
    # Fire the entire script into your Mac in one single shot
    subprocess.run(["osascript", "-e", applescript], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)