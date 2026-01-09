def nested_lists(*args: list):
    list1 = []
    for i in range(len(args)):
        for j in args:
            list1.append(j)
        break
    return list1