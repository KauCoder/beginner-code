print("If you don't mind, we will be asking you a few questions. Thank you.")

def main():
    try:
        name = input("What is your name? ")
        while name == "":
            print("Name is required.")
            name = input("What is your name? ")
        age = int(input(f"Hello, {name}, how old are you? "))
        while age == "":
            print("Age is required.")
            age = int(input(f"How old are you, {name}? "))
        if age >= 18:
            print("Ok, one more question,\n\n")
            country = input("What country are you from? ")
            if country.lower() == "canada":
                print("Great! You are eligible to vote! Have a nice day!")
            elif country.lower() == "united states of america" or "usa" or "united states" or "america":
                print("GET OUT YOU STUPID AMERICAN! YOU DO NOT BELONG IN THIS COUNTRY!!!")
                print("You are not thanked for coming to VoteCheck.")
                exit()
            else:
                print(f"Sorry, you're not eligible to vote in {country}.")
        else:
            print("Sorry. You are too young to vote yet. Come back when you are 18 or more. Have a nice day!")
    except ValueError:
        print("Numbers Only!")
    except Exception as a:
        print(f"Sorry. Something went wrong.\n\n{a}")

main()

print("Thank you for coming to VoteCheck!!!")