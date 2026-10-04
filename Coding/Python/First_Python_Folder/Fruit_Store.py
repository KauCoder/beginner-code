class Fruit:
    def __init__(self, type: str, cost: float):
        self.type = type.lower()
        self.cost = cost
        self.bought: bool = False

    def buy(self):
        self.bought = True

    def __str__(self):
        return f"This {self.type} costs ${self.cost}."

Fruits = {
    "apple": Fruit("apple", 0.30),
    "banana": Fruit("banana", 0.30),
    "cherry": Fruit("cherry", 0.30),
    "watermelon": Fruit("watermelon", 2)
}

def main():
    while True:
        input("Welcome to KFruits Fruits Store! (Press \"Enter\" to continue)")
        request = input("What would you like to buy today (Say \"items\" to see the fruits in stock today)? ").lower()
        if request == "items":
            for k, v in Fruits.items():
                print(v)
        elif request in Fruits.keys():
            print(f"That will cost {Fruits.get(request)}")
        else:
            print("That item is not on the list. Please try again.")

if __name__ == "__main__":
    main()