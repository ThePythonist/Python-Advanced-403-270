import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print((self.length + self.width) * 2)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(self.radius * self.radius * math.pi)

    def perimeter(self):
        print(self.radius * 2 * math.pi)


# Polymorphic Method

def show_area(shape):
    print(f"Area of {shape.__class__}", end=" : ")
    shape.area()


def show_per(shape):
    print(f"Perimeter of {shape.__class__}", end=" : ")
    shape.perimeter()


shape1 = Rectangle(7, 10)
shape2 = Circle(6)

show_per(shape2)
