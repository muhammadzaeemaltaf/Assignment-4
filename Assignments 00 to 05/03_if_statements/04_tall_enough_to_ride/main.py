def tall_enough(height):
    min_required_height = 50

    if height >= min_required_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


def main():
    while True:
        height_input = input("How tall are you? ")  

        if height_input == "":  
            break

        try:
            height = int(height_input)  
            tall_enough(height)
        except ValueError:
            print("Please enter a valid number.")  

if __name__ == '__main__':
    main()
