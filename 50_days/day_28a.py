def index_position(a):
    idex = []
    for i, item in enumerate(a):
        if item.islower():
            idex.append(i)
    return idex


print(index_position('LovE'))