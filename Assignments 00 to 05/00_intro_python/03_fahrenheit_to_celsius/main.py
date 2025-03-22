def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()
