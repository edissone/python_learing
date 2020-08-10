from src.polygons.Triangle import *


def test_versatile_triangle_sides(versatile):
    assert versatile.sides == (1, 4, 7)

def test_versatile_triangle_type(versatile):
    assert versatile.angle_type == TriangleType.VERSATILE


def test_versatile_perimeter(versatile):
    assert versatile.perimeter == 12


def test_versatile_area(versatile):
    assert versatile.area == 190.49409439665052


def test_equilateral_triangle_sides(equilateral):
    assert equilateral.sides == (3, 3, 3)


def test_equilateral_triangle_type(equilateral):
    assert equilateral.angle_type == TriangleType.EQUILATERAL


def test_equilateral_perimeter(equilateral):
    assert equilateral.perimeter == 9


def test_equilateral_area(equilateral):
    assert equilateral.area == 105.2220865598093


def test_rectangular_triangle_sides(rectangular):
    assert rectangular.sides == (3, 4, 5)


def test_rectangular_triangle_type(rectangular):
    assert rectangular.angle_type == TriangleType.RECTANGULAR


def test_rectangular_perimeter(rectangular):
    assert rectangular.perimeter == 12


def test_rectangular_area(rectangular):
    assert rectangular.area == 278.854800926934

def test_change_sides(rectangular, versatile):
    rectangular.sides = versatile.sides
    assert rectangular.sides == versatile.sides
