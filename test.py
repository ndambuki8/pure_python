#Python decorator is a function that takes in a function and returns it by add some 
# functionality
def make_pretty(func):
    #define the inner function
    def inner():
        #add some additional behavior to decorated function
        print("I got decorated")

        #call the original function
        func()
    #return the inner function
    return inner()

#define the ordinary function
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()