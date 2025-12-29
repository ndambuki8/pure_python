def sum_list(lst1: list):
    counta = 0
    for items in lst1:
        for i in items:
            counta += i
    return 'The sum is ', counta

print(sum_list([2,4,5,6], [2,3,4,5]))