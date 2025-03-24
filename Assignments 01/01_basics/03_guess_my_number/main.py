from random import randint

def main():
    secret_number: int = randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    guess = input("What's your guess? ")
    while True:
        if guess == "":
            break
        try:
            guess = int(guess)
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print("You've guessed it! My number was " + str(secret_number))
                break

            print("")
            guess = input("What's your guess? ")
        except ValueError:
            print("Please enter a number")
            guess = input("What's your guess? ")


    
if __name__ == "__main__":
    main()