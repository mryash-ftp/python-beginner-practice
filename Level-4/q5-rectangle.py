class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))

v = Rectangle(20, 50)
v.area()
v.perimeter()
