import inquirer
from time import sleep

def loading(times, /):
    for _ in range(times):
        print("Loading", end="")
        sleep(0.2)
        print("\r", end="")
        print("Loading.", end="")
        sleep(0.2)
        print("\r", end="")
        print("Loading..", end="")
        sleep(0.2)
        print("\r", end="")
        print("Loading...", end="")
        print("\r", end="")

# Bank Program

class User:
    def __init__(self, savings_account: float, normal_account: float, balance: float):
        self.savings_account = savings_account
        self.normal_account = normal_account
        self.balance = round(balance)
        normal_account = balance
    
    def deposit(self, deposit_amount=0, /):
        sleep(0.5)
        self.balance += deposit_amount
        print("Deposit complete.")

        
    def withdraw(self, withdraw_amount=0, /):
        sleep(0.5)
        self.balance -= withdraw_amount
        print("Withdraw complete.")

    def addToSavings(self, savings_amount):
        self.savings_amount = savings_amount
        balance -= savings_amount
Kaushal = User(50000000.00, 25000000.00, 83000)

input("Welcome to Kwick Banking!!!\nPress CTRL+C at any time to quit.\nPress enter to continue: ")

answer = 0

def menu():
    global answer

    sleep(0.5)

    print()
    
    inquirer.List("prompts",
                message="*--------- MENU ---------*",
                choices=["Deposit", "Withdraw", "Add To Savings Account", "View Account", "View Savings Account"]                                  
    )
    answer = inquirer.prompt("prompts")
    sleep(0.5)

def main():
    if answer.get("Deposit"):
        try:
            deposit_input = float(input("How much money do you want to deposit? $"))
        except ValueError:
            print("That is not a money amount.")
        User.deposit(deposit_input)
    elif answer.get("Withdraw"):
        try:
            withdraw_input = float(input("How much money do you want to withdraw? $"))
            User.withdraw(withdraw_input)
        except ValueError:
            print("That is not a money amount.")
        except withdraw_input > User.balance:
            print("You do not have enough money to withdraw that amount.")
    elif answer.get("Add To Savings Account"):
        try:
            add_savings = int(input("How much money do you want to add to your savings? "))
        except ValueError:
            print("That is not a money amount")
        except add_savings > User.normal_account:
            print("That amount is too much; you do not have enough money.")
        User.addToSavings()