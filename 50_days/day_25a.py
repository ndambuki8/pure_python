def all_the_same(a):
    a = all(i == a[0] for i in a)
    return a

print(all_the_same(["Mary", "Mary", "Mary"]))


def all_the_same2(a):
    for i, item in enumerate(a):
        if item[i] == item[0]:
            return True
        else:
            return False
        
print(all_the_same2(['Mary', 'Mary', 'Mary']))