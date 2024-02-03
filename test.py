#difference between type() and instance()

class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def area(self):
        pass

obj1 = Polygon()
obj2 = Triangle()

print(type(obj2) == Triangle)
print(type(obj2) == Polygon)

print(isinstance(obj1,Polygon))
print(isinstance(obj2, Polygon))