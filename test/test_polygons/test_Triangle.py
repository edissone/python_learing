from polygons.Triangle import *


def test_versatile_triangle_sides():
    # setup
    triangle1 = Triangle((1, 4, 7))

    # assertion
    assert triangle1.sides == (1, 4, 7)

def test_versatile_triangle_type():
    # setup
    triangle1 = Triangle((1, 4, 7))

    # assertion
    assert triangle1.angle_type == TriangleType.VERSATILE


def test_versatile_perimeter():
    # setup
    triangle1 = Triangle((1, 4, 7))

    # assertion
    assert triangle1.perimeter == 12


def test_versatile_area():
    # setup
    triangle1 = Triangle((1, 4, 7))

    # assertion
    assert triangle1.area == 190.49409439665052


def test_equilateral_triangle_sides():
    # setup
    triangle2 = Triangle((3, 3, 3))

    # assertion
    assert triangle2.sides == (3, 3, 3)


def test_equilateral_triangle_type():
    # setup
    triangle2 = Triangle((3, 3, 3))

    # assertion
    assert triangle2.angle_type == TriangleType.EQUILATERAL


def test_equilateral_perimeter():
    # setup
    triangle2 = Triangle((3, 3, 3))

    # assertion
    assert triangle2.perimeter == 9


def test_equilateral_area():
    # setup
    triangle2 = Triangle((3, 3, 3))

    # assertion
    assert triangle2.area == 105.2220865598093


def test_rectangular_triangle_sides():
    # setup
    triangle3 = Triangle((3, 4, 5))

    # assertion
    assert triangle3.sides == (3, 4, 5)


def test_rectangular_triangle_type():
    # setup
    triangle3 = Triangle((3, 4, 5))

    # assertion
    assert triangle3.angle_type == TriangleType.RECTANGULAR


def test_rectangular_perimeter():
    # setup
    triangle3 = Triangle((3, 4, 5))

    # assertion
    assert triangle3.perimeter == 12


def test_rectangular_area():
    # setup
    triangle3 = Triangle((3, 4, 5))

    # assertion
    assert triangle3.area == 278.854800926934

def test_change_sides():
    # setup
    triangle1 = Triangle((1, 4, 7))
    triangle2 = Triangle((3, 3, 3))

    # assertion
    triangle1.sides = triangle2.sides
    assert triangle1.sides == triangle2.sides
