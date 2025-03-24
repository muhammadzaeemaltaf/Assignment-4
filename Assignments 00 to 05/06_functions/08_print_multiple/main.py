def print_multiple(message, repeats):
        print((message + ' ') * repeats)

def main():
    user_input = input("Enter a message: ")
    user_repeats = int(input("Enter the number of times to repeat: "))

    print_multiple(user_input, user_repeats)


if __name__ == "__main__":
    main()