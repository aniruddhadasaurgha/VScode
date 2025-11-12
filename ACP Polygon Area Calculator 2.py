class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
def compute_area(s):
    return s.area()
rect = rectangle(10, 5)
tri = triangle(8, 6)
sqr = square(4)
print(f"The area of the rectangle is: {compute_area(rect)}")
print(f"The area of the triangle is: {compute_area(tri)}")
print(f"The area of the square is: {compute_area(sqr)}")
print(f"The area of the polygon is: {compute_area(rect) + compute_area(tri) + compute_area(sqr)}")
