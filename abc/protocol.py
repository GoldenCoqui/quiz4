from typing import Protocol, Optional

class ShapeProtocol(Protocol):
    def calculate_area(self) -> float:
        pass

    def display_info(self) -> None:
        pass

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

    def display_info(self) -> None:
        print(f"Circle with radius {self.radius}")

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def display_info(self) -> None:
        print(f"Rectangle with length {self.length} and width {self.width}")

# Example usage
def print_info(shape: ShapeProtocol) -> None:
    area = shape.calculate_area()
    shape.display_info()
    print(f"Area: {area}\n")

circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

print_info(circle)
print_info(rectangle)
