def main():
    print("Welcome to the Mad Libs game!")
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    
    story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was an unforgettable adventure!"
    
    print("\nHere is your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    main()
