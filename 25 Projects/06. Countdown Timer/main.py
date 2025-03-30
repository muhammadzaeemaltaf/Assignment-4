import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") 
        time.sleep(1)
        t -= 1
    print("Time's up!")


t = input("Enter the time in seconds: ")

try:
    t = int(t)
    if t < 0:
        raise ValueError("Time must be a positive integer.")
    
    countdown(t)
except ValueError as e:
    print(f"Invalid input: Please enter a positive integer.")


