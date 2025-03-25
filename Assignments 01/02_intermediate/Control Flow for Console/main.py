from random import randint

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")

    user_score = 0

    for i in range(NUM_ROUNDS):
        print('--------------------------------')
        print(f"Round {i+1}/5")
        print('--------------------------------')

        computer_guess = randint(1, 100)
        user_guess = randint(1, 100)
        print(f"Your number is {user_guess}")
        

        ask = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        if ask == "":
            print("")
            print("Thanks for playing!")
            print(f"Your score is now {user_score}")
            return


        higher = computer_guess < user_guess and ask == "higher"
        lower = computer_guess > user_guess and ask == "lower"

        if(higher or lower):
            print(f"You were right! The computer's number was {computer_guess}")
            user_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_guess}")

        print('--------------------------------')
        print(f"Your score is now {user_score}")
        



if __name__ == "__main__":
    main()