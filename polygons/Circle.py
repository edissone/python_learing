from polygons.Polygon import Polygon
from math import pow, pi


class Circle(Polygon):

    def __init__(self, radius: int):
        if not isinstance(radius, int):
            raise TypeError("Radius have to be an integer")
        self._radius = radius

    def area(self):
        return pow(self._radius, 2) * pi

    @property
    def radius(self):
        return self._radius
