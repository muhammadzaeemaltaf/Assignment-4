from random import choice


print("Welcome to Password Generator")
print("==============================")
print("")

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.<>?/0123456789'

number = int(input("Enter the number of passwords you want to generate: "))
length = int(input("Enter the length of the password: "))


def genrate_password(no, l):
    while no > 0:
        password = ''
        for _ in range(l):
            password += choice(char)
        print(password)
        no -= 1



print("Your Passwords are:")

genrate_password(number, length)