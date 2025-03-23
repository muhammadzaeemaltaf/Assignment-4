def read_phonebook():

    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name.lower() == "":
            break
        number = input("Enter a number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_phonenook(phonebook):
     while True:
        name = input("Enter a name to lookup: ")
        if name.lower() == "":
            break
        if name in phonebook:
            print(str(name) + " -> " + str(phonebook[name]))
        else:
            print("Name not found in phonebook.")


def main():
    phonebook = read_phonebook()
    print_phonebook(phonebook)
    lookup_phonenook(phonebook)


if __name__ == "__main__":
    main()