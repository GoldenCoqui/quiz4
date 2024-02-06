from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def display_info(self):
        print(f"Circle with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def display_info(self):
        print(f"Rectangle with length {self.length} and width {self.width}")

# Example usage
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

print("Circle Area:", circle.calculate_area())
circle.display_info()

print("\nRectangle Area:", rectangle.calculate_area())
rectangle.display_info()
