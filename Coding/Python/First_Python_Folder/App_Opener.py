import subprocess
from sys import exit
from time import sleep

x: int = 1
app_input: int = 0

def open_app(app_name) -> None:

    global x

    while x == 1:
        try:

            subprocess.run(["open", "-a", app_name], check=True)
            x = 0

        except app_name == "":
            print("App name can not be empty!")
        except subprocess.CalledProcessError:
            sleep(0.1)
            print(f"Failed to open {app_name}. Check if you misspelled your app name.")
if __name__ == "__main__":
    open_app(input("> "))