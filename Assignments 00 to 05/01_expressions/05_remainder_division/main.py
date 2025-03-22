def main():
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))

    quotient: int = num1 // num2
    remainder: int = num1 % num2

    print(f"{num1} divided by {num2} is {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
    main()
