from microbit import *  # type: ignore

x = 3

# Dictionary mapping position to image pattern
STICK_FIGURES = {
    1: "00000:70000:77000:70000:07000:",
    2: "00000:07000:77700:07000:70700:",
    3: "00000:00700:07770:00700:07070:",
    4: "00000:00070:00777:00070:00707:",
    5: "00000:00007:00077:00007:00070:",
}

while True:
    if button_a.is_pressed() and x > 1:  # type: ignore
        x -= 1
        while button_a.is_pressed():  # type: ignore
            sleep(10)  # type: ignore

    if button_b.is_pressed() and x < 5:  # type: ignore
        x += 1
        while button_b.is_pressed():  # type: ignore
            sleep(10)  # type: ignore

    # Use dictionary to display the appropriate image
    display.show(Image(STICK_FIGURES[x]))  # type: ignore