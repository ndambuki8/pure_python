#Python program to Display Powers of 2 using Anonymous function

terms = 10

result = list(map(lambda x: 2 ** x, range(terms)))
print(terms)

for i in range(terms):
    print("2 power", i, "is", result[i])