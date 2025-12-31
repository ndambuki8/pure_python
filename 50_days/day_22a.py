def add_hash(a: str):
    print("#".join(a))
    return "#".join(a)


def add_underscore(a: str):
    print(str(a).replace("#", "_"))
    return str(a).replace("#", "_")

def remove_underscore(a: str):
    return str(a).replace("_", "")

print(remove_underscore(add_underscore(add_hash('Python'))))