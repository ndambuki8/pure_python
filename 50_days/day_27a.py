def uniq_numbers(a: list):
    list1 = []
    for number in a:
        if number not in list1:
            list1.append(number)
    dif = sum(a) - sum(list1)
    if dif % 2 == 0:
        return a
    else:
        return list1
    

print(uniq_numbers([1,2,4,5,6,7,8,8]))