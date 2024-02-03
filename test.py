#getting the class name of an instance

class Vehicle:
    def name(self, name):
        return name
    
v = Vehicle()
print(type(v).__name__)