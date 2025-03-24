def count_even(lst):
    count = 0

    for num in lst:
        if num % 2 == 0:
            count += 1

    print(count)



def get_lst():
    lst = []
    while True:
        user_input = input("Enter a number or press Enter to stop: ") 
        if user_input == "":  
            break
        try:
            lst.append(int(user_input)) 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return lst

def main():
    lst = get_lst()
    count_even(lst)


if __name__ == "__main__":
    main()