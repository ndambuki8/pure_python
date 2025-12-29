def convert_list(lst1: list):
    list1 = []
    for items in lst1:
        for i in items:
            list1.append(i)
    return list1

print(convert_list([[2,4,5,6]]))