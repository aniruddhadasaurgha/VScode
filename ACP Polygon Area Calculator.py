from abc import ABC, abstractmethod
class Polygon(ABC):
    
 def __init__(self, name):
        self.name = name
        def area(self):
            pass
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side
def calculate_area(polygon):
    return polygon.area()
rect = Rectangle(10, 5)
tri = Triangle(8, 6)
sqr = Square(4)
print(f"The area of the {rect.name} is: {calculate_area(rect)}")
print(f"The area of the {tri.name} is: {calculate_area(tri)}")
print(f"The area of the {sqr.name} is: {calculate_area(sqr)}")
    
