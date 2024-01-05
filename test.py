#Python generators expression - a concise way to create a generator object

def PowTwo(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1