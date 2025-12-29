import random

num = random.randint(0,10)

def user_name():
    name = input('Enter name: ')
    name = name[::-1]
    username = name + str(num)
    return username

print(user_name())