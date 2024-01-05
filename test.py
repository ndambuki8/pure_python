#Python generators expression - a concise way to create a generator object

#create the generator object
squares_generator = (i * i for i in range(5))

#iterate over the generator and print the values
for i in squares_generator:
    print(i)