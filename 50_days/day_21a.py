def make_tuples(a,b):
    a = zip(a,b)
    return list(tuple(a))

print(make_tuples([1,2,3,4], [5,6,7,8]))