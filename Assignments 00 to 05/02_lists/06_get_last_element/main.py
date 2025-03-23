def get_last_element(lst):
    print(lst[-1])  # Print the last element of the list

def get_list():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)

if __name__ == '__main__':
    main()
