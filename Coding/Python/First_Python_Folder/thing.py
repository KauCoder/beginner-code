import time
length = 10
while True:
    for i in range(length + 1):
        equals = '=' * (length - i)
        dashes = '-' * i
        print(f"{i}|{equals}{dashes}|", end="\r", flush=True)
        time.sleep(1)
    break