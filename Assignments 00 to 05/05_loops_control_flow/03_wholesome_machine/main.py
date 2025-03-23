AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")
    while True:
        user_input = input()
        if user_input == AFFIRMATION:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please type the following affirmation:")

if __name__ == "__main__":
    main()
