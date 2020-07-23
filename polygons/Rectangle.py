from enum import Enum
from polygons.Polygon import Polygon


class RectangleType(Enum):
    SQUARE = 0
    RECTANGLE = 1

class Rectangle(Polygon):

    def __init__(self, sides: tuple):
        if not len(sides) == 2:
            raise ValueError("Rectangle must take 2 arguments")
        super().__init__(sides)

    def area(self):
        result = 1
        for side in self._sides:
            result *= side
        return result

    @property
    def type(self):
        if self._sides[0] == self._sides[1]:
            return RectangleType.SQUARE
        else:
            return RectangleType.RECTANGLE

if __name__ == "__main__":
    rect_sides = (2, 4)
    rect = Rectangle(rect_sides)

    print(f"Rectangle sides: {rect.sides}")
    print(f"Rectangle type: {rect.type}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    print(f"Rectangle area: {rect.area()}\n")

    square_sides = (2, 2)
    square = Rectangle(square_sides)
    print(f"Square sides: {square.sides}")
    print(f"Square type: {square.type}")
    print(f"Square perimeter: {square.perimeter()}")
    print(f"Square area: {square.area()}")
