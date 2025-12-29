def convert_numbers(n):
    new_list = []
    for num in n:
        new_list.append("{:,}".format(num))
    return new_list


print(convert_numbers([1000000, 2356989, 2354672, 9878098]))