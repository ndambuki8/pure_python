def difference(arr1: list, arr2: list):
    # Find items in list1 not in list2
    list1 = [i for i in arr1 if i not in arr2]

    #Find items in list 2 not in list1
    list2 = [j for j in arr2 if j not in arr1]

    #concatenate the two lists

    final_list = list1 + list2

    return final_list