def count_characters(a):
    a = a.replace(' ', '')
    return f'The string has ' \
         f'{len(a)} elements'

print(count_characters('I love learning'))