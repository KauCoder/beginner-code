while True:

    # ---------- THIS IS THE CALCULATOR (THE REST IS JUST RESTART HANDLING) ---------- #
    print(eval(input("Enter a mathematical expression (A math question): ")))
    # ---------- THIS IS THE CALCULATOR (THE REST IS JUST RESTART HANDLING) ---------- #

    continue_input = input("Do you want to ask another question? (yes/no): ")
    if continue_input.lower() == 'no':
        break
print("Thank you for using the calculator!")