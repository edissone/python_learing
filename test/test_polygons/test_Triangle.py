from polygons.Triangle import *

triangle1 = Triangle((1, 4, 7))


def test_versatile_triangle_sides():
    assert triangle1.sides == (1, 4, 7)

def test_versatile_triangle_type():
    assert triangle1.angle_type == TriangleType.VERSATILE


def test_versatile_perimeter():
    assert triangle1.perimeter() == 12


def test_versatile_area():
    assert round(triangle1.area()) == 190

triangle2 = Triangle((3, 3, 3))

def test_equilateral_triangle_sides():
    assert triangle2.sides == (3, 3, 3)


def test_equilateral_triangle_type():
    assert triangle2.angle_type == TriangleType.EQUILATERAL


def test_equilateral_perimeter():
    assert triangle2.perimeter() == 9


def test_equilateral_area():
    assert round(triangle2.area()) == 105


triangle3 = Triangle((3, 4, 5))


def test_rectangular_triangle_sides():
    assert triangle3.sides == (3, 4, 5)


def test_rectangular_triangle_type():
    assert triangle3.angle_type == TriangleType.RECTANGULAR


def test_rectangular_perimeter():
    assert triangle3.perimeter() == 12


def test_rectangular_area():
    assert round(triangle3.area()) == 279

def test_change_sides():
    triangle1.sides = triangle2.sides
    assert triangle1.sides == triangle2.sides
