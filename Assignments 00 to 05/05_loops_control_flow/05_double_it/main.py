def double_it(number):
    while number < 100:
        number *= 2
        print(number, end=" ")

def main():
    curr_value = int(input("Enter a number: "))

    double_it(curr_value)


if __name__ == "__main__":
    main()