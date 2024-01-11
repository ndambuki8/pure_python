#Python closures
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

#call the outer function
odd = calculate()
print(odd())
print(odd())
print(odd())

#call outer functioo again
odd2 = calculate()
print(odd2())