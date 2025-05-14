class Point(object):
    def __new__(cls, *args, **kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)

        # create our object and return it
        obj = super().__new__(cls)
        return obj
    
    def __init__(self, x=0, y=0):
        print("From init")
        self.x = x
        self.y = y


# p2 = Point(3,4)
# p2

class SqPoint(Point):
    MAX_Inst = 4
    Inst_created = 0

    def __new__(cls, *args, **kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1
        return super().__new__(cls)
    
p1 = SqPoint(0,0)
p1
p2 = SqPoint(1,0)
p2
p3 = SqPoint(1,1)
p3
p4 = SqPoint(0,1)
p4
p5 = SqPoint(2,2)
p5