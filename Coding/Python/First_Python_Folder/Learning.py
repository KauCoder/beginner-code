for i in range(4, 21):
    candies = 90 / i

    if candies.is_integer():
        print(f"{candies}, valid")
    else:
        print(f"{candies}, invalid")