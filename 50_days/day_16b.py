nested_list = [[12,34,56,67], [34,68,78]]

new_list = []

# A nested for loop to access the inner list
for arr in nested_list:
    for num in arr:
        #create a list of numbers wanted
        if num in [34,67,78]:
            #checking if number is already existing before appendinng
            if num not in new_list:
                new_list.append(num)


print(new_list)