def sumOfNumbers(numbers: list) -> int:
    sum = 0
    for number in numbers:
        sum += number
    return sum

def main():
    numbers = [1, 2, 3, 4, 5]
    print(sumOfNumbers(numbers))

if __name__ == "__main__":
    main()