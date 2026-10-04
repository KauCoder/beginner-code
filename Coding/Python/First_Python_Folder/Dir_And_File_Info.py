import os
import sys
import inquirer as iq
questions = [iq.List("question",
                    
                message="Choose one the following questions to ask",
                choices = ["What directory are we in?", "What is the current file name?", "Does this file exist?", "Nevermind"]    
                    
                    
                )
]
answers = iq.prompt(questions)
if answers["question"] == "What directory are we in?":
    sys.stdout.write("The current directory we are in is called: ")
    sys.stdout.write(os.getcwd() + "\n")
elif answers["question"] == "What is the current file name?":
    sys.stdout.write("The name of the file we are in right now is: ")
    sys.stdout.write(os.path.basename(__file__) + "\n")
elif answers["question"] == "Does this file exist?":
    file_name = input("Enter the file name to check if it exists: ")
    if os.path.exists(file_name):
        print(f"The file '{file_name}' exists.")
    else:
        print(f"The file '{file_name}' does not exist.")
elif answers["question"] == "Nevermind":
    print("Goodbye!")
    sys.exit(0)
else:
    sys.stderr("That is not a valid option.")
    sys.exit()