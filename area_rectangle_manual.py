#area of rectangle manual
#write python code to find area and perimeter of a rectangle, use less comments and no docstrings
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
# Get user input
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
rect = Rectangle(l, b)
print("Area of the rectangle:", rect.area())
print("Perimeter of the rectangle:", rect.perimeter())
