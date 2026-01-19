def all_the_same(a):
    a = all(i == a[0] for i in a)
    return a

print(all_the_same(["Mary", "Mary", "Mary"]))