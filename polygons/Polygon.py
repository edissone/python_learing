from abc import ABC, abstractmethod


class Polygon(ABC):

    def __init__(self, sides: tuple):
        self._sides = sides

    @property
    def perimeter(self):
        result = 0
        for side in self._sides:
            result += side
        return result

    @abstractmethod
    def area(self):
        pass  # formula for calculating an arbitrary polygon?

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, values: tuple):
        self._sides = values
