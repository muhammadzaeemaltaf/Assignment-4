def main():
    PeturksbouipoAge = 16
    StanlauAge = 25
    MayenguaAge = 48

    age = int(input("How old are you? "))

    if age >= PeturksbouipoAge:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= StanlauAge:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= MayenguaAge:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")


if __name__ == "__main__":
    main()
