str1 = "the love is real"

def read_backwards(n: str) -> str:
    # create an empty list
    x = []
    for i in n.split() [::-1]: # using split to split string on whitespaces
        x.append(i)
    # using the join method to join string
    return ' '.join(x)

print(read_backwards(str1))