import os
from time import sleep

os.system("say 'What is your name? '")
for l in "What is your name?":
    print(l, end="", flush=True)
    sleep(0.02)

sleep(0.5)

print()

name = input("> ")

while name == "":
    os.system("say 'You seemed to not have entered your name. Please try again.")
    for l in "You seemed to not have entered your name. Please try again.":
        print(l, end="", flush=True)
        sleep(0.02)
    sleep(0.5)
    name = input("> ")

os.system(f"say 'Hello, {name}!!!'")
for l in f"Hello, {name}":
    print(l, end="", flush=True)
    sleep(0.02)

print()