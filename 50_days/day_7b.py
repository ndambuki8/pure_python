names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

d = {} # creating an empty dictionary
for name in names:
    if name.startswith('S'):
        # using the dictionary update method
        d.update({name: names.count(name)})

print(d)


# or

from collections import Counter

count = [] # creating an empty list 
for name in names:
    if name.startswith("S"):
        # appending names that start with S to the list
        count.append(name)

    names = Counter(count)

print(names)