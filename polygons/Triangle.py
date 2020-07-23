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

    def area(self):
        result = p = self.perimeter() / 2
        for side in self._sides:
            result *= p * side
        return sqrt(result)

    @property
    def type(self):
        if (self._sides[0] + self._sides[1] + self._sides[2]) / 3 == self._sides[0]:
            return TriangleType.EQUILATERAL
        elif pow(self._sides[0], 2) + pow(self._sides[1], 2) == pow(self._sides[2], 2) \
                or pow(self._sides[1], 2) + pow(self._sides[2], 2) == pow(self._sides[0], 2) \
                or pow(self._sides[0], 2) + pow(self._sides[2], 2) == pow(self._sides[1], 2):
            return TriangleType.RECTANGULAR
        else:
            return TriangleType.VERSATILE


if __name__ == "__main__":
    triangle1_sides = (3, 3, 3)
    triangle1 = Triangle(triangle1_sides)

    print(f"Triangle sides: {triangle1.sides}")
    print(f"Triangle type: {triangle1.type}")
    print(f"Triangle perimeter: {triangle1.perimeter()}")
    print(f"Triangle area: {triangle1.area()}\n")

    triangle2_sides = (3, 4, 5)
    triangle2 = Triangle(triangle2_sides)

    print(f"Triangle sides: {triangle2.sides}")
    print(f"Triangle type: {triangle2.type}")
    print(f"Triangle perimeter: {triangle2.perimeter()}")
    print(f"Triangle area: {triangle2.area()}\n")

    triangle3_sides = (2, 4, 2)
    triangle3 = Triangle(triangle3_sides)

    print(f"Triangle sides: {triangle3.sides}")
    print(f"Triangle type: {triangle3.type}")
    print(f"Triangle perimeter: {triangle3.perimeter()}")
    print(f"Triangle area: {triangle3.area()}\n")
