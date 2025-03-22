import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    die1, die2 = roll_dice()

    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {die1 + die2}")


if __name__ == '__main__':
    main()