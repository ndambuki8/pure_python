names = ["kerry", "dickson", "John", "Mary", "carol", "'Rose", "adam"]

# creating an empty list
d = []

# using sorted function to sort list in descending order
for name in sorted(names, reverse=True):
    if name.islower():
        d.append(name)
        tuple_names = tuple(d)

print(tuple_names)