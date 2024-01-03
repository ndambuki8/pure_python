#Python infinite iterators
from itertools import count

#create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

#print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))