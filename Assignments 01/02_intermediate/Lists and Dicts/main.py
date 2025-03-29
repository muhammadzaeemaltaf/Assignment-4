def main():
    # Problem 1: Fruit List Operations
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print(f"Initial fruit list length: {len(fruit_list)}")

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print(f"Updated fruit list: {fruit_list}")


def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Index out of range."


def modify_element(lst, index, new_value):
    """Modifies the element at the given index or returns an error message if out of range."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Index out of range. No modification made."


def slice_list(lst, start, end):
    """Returns a sliced portion of the list based on the given range."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return f"Sliced list: {lst[start:end]}"
    return "Invalid range for slicing."


def index_game():
    """Interactive game for list operations."""
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print(access_element(sample_list, index))

        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(sample_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(sample_list, start, end))

        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
    index_game()
