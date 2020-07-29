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

if __name__ == "__main__":
    triangle1_sides = (3, 3, 3)
    triangle1 = Triangle(triangle1_sides)

    print(f"Triangle sides: {triangle1.sides}")
    print(f"Triangle type: {triangle1.angle_type}")
    print(f"Triangle perimeter: {triangle1.perimeter()}")
    print(f"Triangle area: {triangle1.area()}\n")

    triangle2_sides = (3, 4, 5)
    triangle2 = Triangle(triangle2_sides)

    print(f"Triangle sides: {triangle2.sides}")
    print(f"Triangle type: {triangle2.angle_type}")
    print(f"Triangle perimeter: {triangle2.perimeter()}")
    print(f"Triangle area: {triangle2.area()}\n")

    triangle3_sides = (2, 4, 2)
    triangle3 = Triangle(triangle3_sides)

    print(f"Triangle sides: {triangle3.sides}")
    print(f"Triangle type: {triangle3.angle_type}")
    print(f"Triangle perimeter: {triangle3.perimeter()}")
    print(f"Triangle area: {triangle3.area()}\n")
