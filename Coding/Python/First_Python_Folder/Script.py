import time
from pynput import keyboard
import extensionslib

TAUMATA = "taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronokupokaiwhenuakitanatahu"
CHARG = "chargoggagoggmanchauggagoggchaubunagungamaugg"
LLANFAIR = "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"

def trigger(word):
    extensionslib.script_type_virtual(word)

def on_press(key):
    if key == keyboard.Key.f6:
        trigger(CHARG)
    if key == keyboard.Key.f7:
        trigger(TAUMATA)
    if key == keyboard.Key.f8:
        trigger(LLANFAIR)
    if key == keyboard.Key.esc:
        print("\n[-] Shutting down macro loop.")
        return False

print("==================================================")
print("► AppleScript Global Macro Active.")
print("► 1. Click completely inside your game chat, Discord, or TextEdit.")
print("► Press 'ESC' inside your Terminal to turn it off.")
print("==================================================")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()