from enum import Enum
from polygons.Polygon import Polygon
from math import sqrt, pow

class TriangleType(Enum):
    VERSATILE = 0
    EQUILATERAL = 1
    RECTANGULAR = 2


class Triangle(Polygon):

    def __init__(self, sides: tuple):
        if not len(sides) == 3:
            raise ValueError("Triangle must take 3 arguments")
        super().__init__(sides)

    @property
    def area(self):
        result = p = self.perimeter() / 2
        for side in self._sides:
            result *= p * side
        return sqrt(result)

    @property
    def angle_type(self):
        a, b, c = self._sides
        if (a + b + c) / 3 == a:
            triangle_type = TriangleType.EQUILATERAL
        elif pow(a, 2) + pow(b, 2) == pow(c, 2) \
                or pow(b, 2) + pow(c, 2) == pow(a, 2) \
                or pow(a, 2) + pow(c, 2) == pow(b, 2):
            triangle_type = TriangleType.RECTANGULAR
        else:
            triangle_type = TriangleType.VERSATILE
        return triangle_type
