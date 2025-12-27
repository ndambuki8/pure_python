def divide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return f'The square-root of the number is {sq_root}'
    else:
        remainder = number % 5
        return f'The remainder of the division is {remainder}'
    
print(divide_or_square(10))