class Circle:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        pi=3.1416
        print(pi*self.rad*self.rad)
    def perimeter(self):
        print(2*3.1416*self.rad)


c1=Circle(5)
c1.area()
c1.perimeter()
        