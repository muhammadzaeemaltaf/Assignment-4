C = 299792458  # Speed of light in m/s


def main():

    try:
        mass = float(input("Enter kilos of mass: "))
        energy = mass * C**2  # E = m * c^2

        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
