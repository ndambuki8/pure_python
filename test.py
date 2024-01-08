#Python closures
def greet(name):
    name = 'John'
    return lambda : "Hi " + name

message = greet()

print(message())