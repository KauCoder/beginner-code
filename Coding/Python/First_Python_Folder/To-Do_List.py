import inquirer as inq

lst = []

while True:

    Menu = [
                inq.List("Menu",
                         message="What would you like to do?",
                         choices=["Add", "Remove", "View", "Exit"],
        ),
    ]
    answer = inq.prompt(Menu)

    if answer["Menu"] == "Add":
        addInput = input("Name of task: ")

        if addInput != "":
            lst.append(addInput)
            input(f"\"{addInput}\" has been added. Press enter to see list: ")
            print(lst, end="\n")
            input("Press enter to return to menu: ")
        else:
            print("Task not found: Did not change anything")
            input("Press enter to return to menu: ")

    elif answer["Menu"] == "Remove":
        answerRmve = input(f"list: {lst} enter the task number (starts at 0) or type \"nevermind\" to cancel: ")
        if answerRmve.isdigit() and int(answerRmve) > -1 <= len(lst):
            lst.pop(int(answerRmve))
            input("Press enter to return to menu: ")
        elif answerRmve.lower() == "nevermind":
            print("Ok, nothing removed.")
            input("Press enter to return to menu: ")
        else:
            print("Number not valid: Is either not a positive integer or it out of range. Noting removed")
            input("Press enter to return to menu: ")

    elif answer["Menu"] == "View":
        print(lst)
        input("Press enter to return to menu: ")

    elif answer["Menu"] == "Exit":
        confirm = [
            inq.List("answerConfirm",
                message="Are you sure you want to exit: You will lose all data",
                choices=["Yes", "No"],
            )
        ]
        answerConfirm = inq.prompt(confirm)
        if answerConfirm["answerConfirm"] == "Yes":
            print()
            break
        elif answerConfirm["answerConfirm"] == "No":
            print("Ok, exit cancelled")
            input("Press enter to return to menu: ")
print("Thank You For Using My To-Do List!!!")