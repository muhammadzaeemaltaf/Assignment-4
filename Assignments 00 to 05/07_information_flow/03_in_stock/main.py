inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 75,
    "pear": 1000,
    "grape": 200
}


def num_in_stock(fruit):
    return inventory.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
    if count > 0:
        print("This fruit is in stock! Here is how many:" , end=" ")
        print(count)
    else:
        print("This fruit is not in stock.")


if __name__ == "__main__":
    main()  