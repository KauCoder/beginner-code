import random
import inquirer as inq
import sys

while True:
    charsReg = "abcdefghijklmnopqrstuvwxyz"
    charsCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsNum = "1234567890"
    charsSpec = "!@#$%^&*()[]\\;',./{|}:\"<>?`-=~_+"
    charsSSpec = "¡™£¢∞§¶•ªºå∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ®ß†¨√∑≈¥ˀ`–≠“‘«…æ≤≥÷ÅıÇÎ´Ï˝ÓˆÔÒÂ˜Ø∏Œ‰Íˇ¨◊„˛Á¸⁄€‹›ﬁﬂ‡°·‚`—±”’»ÚÆ¯˘¿"

    charsSimple = charsReg + charsCaps + charsNum
    charsHard = charsSimple + charsSpec
    charsComplex = charsHard + charsSSpec

    password = ""

    def passSimple(x):
        """
        Generates a simple password containing capital characters, normal characters, and numbers.
        Minimum characters is 4. Maximum is 6
        """
        for _ in range(x):
            global password
            password += random.choice(charsSimple)

    def passHard(x):
        """
        Generates a hard password containing capital characters, normal characters, numbers, and special characters.
        Minimum characters is 7. Maximum is 11
        """
        for _ in range(x):
            global password
            password += random.choice(charsHard)

    def passComplex(x):
        """
        Generates a complex password containing capital characters, normal characters, numbers, special characters, and more complex characters that some websites may not support.
        Minimum characters is 12. Maximum is 15
        """
        for _ in range(x):
            global password
            password += random.choice(charsComplex)

    questions = [
            inq.List("passDifficulty",
                        message="Select Difficulty (Complexity) of password",
                        choices=["Simple", "Hard", "Complex"],
        ),
    ]
    answers = inq.prompt(questions)
    if answers["passDifficulty"] == "Simple":
        length = [
            inq.List("lenSimple",
                    message="Enter the length of the password",
                    choices=[4, 5, 6]
                    ),
        ]
        answers = inq.prompt(length)
        passSimple(answers["lenSimple"])
    elif answers["passDifficulty"] == "Hard":
        length = [
            inq.List("lenHard",
                    message="Enter the length of the password",
                    choices=[7, 8, 9, 10, 11]
                    ),
        ]
        answers = inq.prompt(length)
        passHard(answers["lenHard"])
    elif answers["passDifficulty"] == "Complex":
        length = [
            inq.List("lenComplex",
                    message="Enter the length of the password",
                    choices=[12, 13, 14, 15]
                    ),
        ]
        answers = inq.prompt(length)
        passComplex(answers["lenComplex"])

    print(f"\n\nYour password is: {password}\n\n")

    restart = [
        inq.List("restartConfirm",
                        message="Do you want to generate another password",
                        choices=["Yes", "No"]
        ),
    ]
    confirmAnswer = inq.prompt(restart)
    if confirmAnswer == "Yes":
        pass
    elif confirmAnswer == "No":
        print("Thank you for using my password generator!!!")
        sys.exit()