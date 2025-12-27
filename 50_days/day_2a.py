def convert_add(list1):
    b = []
    for i in list1:
        b.append(int(i))
    return sum(b)

print(convert_add(['1','3','5']))

#or

def convert_add2(list1: list):
    list2 = []
    count = 0
    for i in list1:
        list2.append(int(i))
    for j in list2:
        count += j
    return count