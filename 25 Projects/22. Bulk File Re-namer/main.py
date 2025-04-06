import os 

def main():
    i = 0
    path = 'D:/Governer IT/Python Assignments/Assignment 4/25 Projects/22. Bulk File Re-namer/'
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            my_dest = f"img_{str(i)}.jpg"  
            my_source = f"{path}{filename}"
            my_dest = f"{path}{my_dest}"
            os.rename(my_source, my_dest)
            i += 1
            print(f"Renamed {my_source} to {my_dest}")
    


if __name__ == '__main__':
    main()