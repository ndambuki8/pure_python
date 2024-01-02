#Python iterators -- __iter__() and __next__()
my_list = [4,7,0]

#create an iterator from the list
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))