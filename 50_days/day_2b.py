def check_duplicates(arr: list):
    for item in arr:
        # using count to find items more than one
        if arr.count(item) > 1:
            return item
        else:
            return 'No duplicates'
        

# lists
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))