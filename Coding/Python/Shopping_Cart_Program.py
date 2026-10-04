print("Welcome to our shopping cart program!")
item = input("What would you like to buy?:\n")
price = float(input("What is the price?:\n"))
quantity = int(input("How many would you like?:\n"))
total = price * quantity

print(f"You have bought {quantity} x {item}\s")
print(f"Your total is:  ${total}")