from random import randint

def main():

    secret_number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    guess = int(input("Enter your guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter your guess: "))

    print(f"Congrats! The number was: {secret_number}")


if __name__ == "__main__":
    main()