import time

def counter():
    num = int(input("Enter a number to count up to ( < 100): "))
    num += 1

    while str(num) == "":
        print("Number not provided")
        num = int(input("Enter a number to count up to ( < 100): "))

    if 0 < num <= 100:
        for i in range(num):
            print(i, end=" ", flush=True)
            time.sleep(0.1)

    while num > 100:
        print("Number too big (Number has to be within 100)")
        num = int(input("Enter a number to count up to ( < 100): "))
        num += 1
        if num <= 100:
            for i in range(num):
                print(i)

try:
    counter()
except ValueError:
    print("Integers only!")
except Exception as e:
    print(f"Sorry, Something went wrong:\n{e}")