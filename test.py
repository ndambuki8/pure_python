#Python generators
def my_generator(n):

    #initialize counter
    value = 0

    #loop until counter is less than n
    while value < n:

        yield value

        value += 1

    
# for value in my_generator(3):
#     print(value)

generator = my_generator(3)
print(next(generator))
print(next(generator))
print(next(generator))