from enum import Enum
from src.polygons.Polygon import Polygon


class RectangleType(Enum):
    SQUARE = 0
    RECTANGLE = 1

class Rectangle(Polygon):

    def __init__(self, sides: tuple):
        if not len(sides) == 2:
            raise ValueError("Rectangle must take 2 arguments")
        super().__init__(sides)

    @property
    def area(self):
        result = 1
        for side in self._sides:
            result *= side
        return result

    @property
    def rect_type(self):
        if self._sides[0] == self._sides[1]:
            return RectangleType.SQUARE
        else:
            return RectangleType.RECTANGLE
