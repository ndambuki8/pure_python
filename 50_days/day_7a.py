def string_range(num:int):
    x = [str(i) for i in range(num)]
    # using join method to add dots 
    x = ".".join(x)
    return x

print(string_range(6))