with open("testfile.txt", "r") as f:
    for lines in f:
        print(lines.strip())