def main():
    fruit_prices = {
        "apple": 5.0,
        "durian": 20.0,
        "jackfruit": 15.0,
        "kiwi": 7.5,
        "rambutan": 10.0,
        "mango": 12.5
    }

    total_cost = 0.0


    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a valid number (0 or more).")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
