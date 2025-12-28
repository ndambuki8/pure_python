def zeros_last(arr: list) -> list:
    i = 0 # settiing index 0
    arr1 = arr
    for num in arr:
        # checking for non-zero numbers
        if num != 0:
            # moving non-zero numnbers too the front of the list
            arr[i] = num
            i += 1

    # moving zero elements to the end of the list
    while i < len(arr):
        arr[i] = 0
        i += 1
        return arr 
    
    else:
        # if no zeroes return originak list in ascending order
        return sorted(arr1)
    

list1 = [1,4,6,0,7,0]
list2 = [2,1,4,7,6]

print(zeros_last(list1))
print(zeros_last(list2))