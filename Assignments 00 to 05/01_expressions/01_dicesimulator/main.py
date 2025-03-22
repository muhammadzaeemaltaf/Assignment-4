import random

global_var = "I'm a global variable"

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Inside roll_dice: Die 1 = {die1}, Die 2 = {die2}")
    return die1, die2  

def main():
    # Roll the dice three times
    for i in range(1, 4):
        die1, die2 = roll_dice()
        print(f"Inside main (Roll {i}): Die 1 = {die1}, Die 2 = {die2} \n")

    print(global_var)  


# Run the program
if __name__ == "__main__":
    main()
