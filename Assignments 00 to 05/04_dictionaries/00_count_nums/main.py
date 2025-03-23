def get_numbers():
    numbers = []
    
    while True:
        num = input("Enter a number (or type 'done' to stop): ")
        if num.lower() == "done":  
            break
        try:
            numbers.append(int(num))  
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    return numbers

def count_occurrences(numbers):
    counts = {}
    
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1   
    return counts

def print_counts(counts):
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

def main():
    numbers = get_numbers()
    counts = count_occurrences(numbers)
    print_counts(counts)

if __name__ == "__main__":
    main()
