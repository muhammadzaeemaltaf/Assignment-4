MAX_LENGTH = 3  

def shorten(lst):
    while len(lst) > MAX_LENGTH:  
        removed_element = lst.pop() 
        print("Removed:", removed_element) 

def get_list():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_list()
    shorten(lst)
    print("Final list:", lst) 


    
if __name__ == '__main__':
    main()
