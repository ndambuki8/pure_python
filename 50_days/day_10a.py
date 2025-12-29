def your_password():
    password1 = input('Enter password')
    password = len(password1) * '*'

    return f'Your password is {password}' \
            f'and its {len(password)} characters long'

print(your_password())