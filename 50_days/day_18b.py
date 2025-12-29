def add_reverse(n: list, k: list):
    # creating an empty list
    new_list = []

    if len(n) == len(k):
        for i in range(0, len(n)):
            # adding and appending corresponding numbers
            new_list.append(n[i] + k[i])
            #3 reversing the new list
            # new_list.reverse()
            new_list = new_list[::-1]
        return new_list
    
    else:
        return f'Lists have different lengths'
    
list1 = [10,12,34]
list2 = [12,56,78]

print(add_reverse(list1, list2))