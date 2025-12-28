def biggest_odd(string1: str):
    odd_nums = [i for i in string1 if int(i) % 2 != 0]
    return f'The biggest odd number is {max(odd_nums)}'

print(biggest_odd('2345659'))