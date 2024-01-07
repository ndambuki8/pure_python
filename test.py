#Python closures
def greet(name):
    def display_name():
        print("Hi", name)

    display_name()

greet("John")