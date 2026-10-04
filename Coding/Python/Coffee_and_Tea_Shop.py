import inquirer

print("\nWelcome to CoffSipGo and TeaSipGo!!!\n")
print("Thank you for coming in today!\n")

store_choice = [inquirer.List("Coffee_or_Tea_Shop",
                              message="Which store do you want to order at? We have CoffSipGo and TeaSipGo!",
                              choices=["CoffSipGo", "TeaSipGo"],
                
                ),
                
                
        ]
answer = inquirer.prompt(store_choice)

if "CoffSipGo" == answer.get("Coffee_or_Tea_Shop"):
    print("Welcome to CoffSipGo Coffee!!!")
    print("Thank you for coming in today!")

    name = input("What is your name?\n") 

    while name == "":
        print("You did NOT enter your name!")
        print("Please enter your name.")
        name = input("What is your name?\n")

    print(f"Oh, hello, {name}!")

    menuCoffee = "Coffee: $2\n Black Coffee: $4\n Latte: $3\n Cappuccino: $4\n CoffSipGo Special: $10"

    order = [inquirer.List("Main_Order",
                message="Choose an item from our menu to order!!!",
                choices=[menuCoffee],
        ), 
    ]                                  
    answer = inquirer.prompt(order)
    print("Great! Your order is coming soon!!!")

if "TeaSipGo" == answer.get("Coffee_or_Tea_Shop"):
    print("Welcome to TeaSipGo Tea!!!")
    print("Thank you for coming in today!")
    
    name = input("What is your name? \n")

    while name == "":
        print("You did NOT enter your name!")
        print("Please enter your name.")
        name = input("What is your name?\n")

    print(f"Oh, hello, {name}!")