import inquirer as inq
import sys

while True:
    print()
    def Calculator(n1, n2, operation):
        def add(n1, n2):
            print(n1 + n2)

        def subtract(n1, n2):
            print(n1 - n2)

        def multiply(n1, n2):
            print(n1 * n2)

        def divide(n1, n2):
            if n2 == 0:
                return "Division by zero is prohibited. Error code: ZeroDivisionError"
            print(n1 / n2)

        def factorial(n):
            if n < 0:
                return "Factorial is not defined for negative numbers."
            if n == 0:
                return 1
            result = 1
            for i in range(1, int(n) + 1):
                result *= i
            print(result)
        input("Welcome to the Calculator App! Press Enter to continue... ")
        try:
            n1 = int(input("Please enter the first number: "))
            n2 = int(input("Please enter the second number (Not required for factorial): "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
        question = [
            inq.List('operation',
                        message="Select an operation",
                        choices=['Add', 'Subtract', 'Multiply', 'Divide', 'Factorial'],
                    ),
        ]
        answers = inq.prompt(question)
        operation = answers['operation']
        if operation == 'Add':
            add(float(n1), float(n2))
        elif operation == 'Subtract':
            subtract(float(n1), float(n2))
        elif operation == 'Multiply':
            multiply(float(n1), float(n2))
        elif operation == 'Divide':
            divide(float(n1), float(n2))
        elif operation == 'Factorial':
            fact_num = int(input("Enter a number to calculate its factorial: "))
            factorial(fact_num)
    try:
        Calculator(0, 0, "")
    except Exception as e:
        print(f"Sorry. Something went wrong.\nError code:\n\n{e}")
    retry = [
        inq.List('retry',
                message="Do you want to retry?",
                choices=['Yes', 'No']
        ),
    ]
    conf = inq.prompt(retry)
    if conf["retry"] == "Yes":
        pass
    elif conf["retry"] == "No":
        sys.exit()