# Opening/Greeting
print("Python is an amazing programming language!\n" + "Here is some information about it!\n\n")

# Opening testfile.txt which has information about Python
with open("testfile.txt") as f:
    for lines in f:
        print(lines.strip())