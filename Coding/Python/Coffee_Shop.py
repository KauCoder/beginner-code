import inquirer
print("Welcome to CoffSipGo coffee!!!")
print("Thank you for coming in today!")
name = input("What is your name? \n") 
while name == "":
    print("You did NOT enter your name!")
    print("Please enter in your name.")
    name = input("What is your name?\n")
print(f"Oh, hello, {name}! ")


menu = "Coffee: $2\n Black Coffee: $4\n Latte: $3\n Cappuccino: $4\n CoffSipGo Special: $10"

order = [ 
    inquirer.List("Main_Order",
                message="Choose an item from our menu to order!!!",
                choices=["Coffee: $2", "Black Coffee: $4", "Latte: $3", "Cappuccino: $4", "CoffSipGo Special: $10"],
    ), 
]                               
answer = inquirer.prompt(order)
print("Great! Your order is coming soon!!!")