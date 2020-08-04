from polygons.Rectangle import *

rect = Rectangle((2, 4))


def test_rectangle_sides():
    assert rect.sides == (2, 4)

def test_rectangle_type():
    assert rect.rect_type == RectangleType.RECTANGLE

def test_rectangle_perimeter():
    assert rect.perimeter() == 6

def test_rectangle_area():
    assert rect.area() == 8

def test_square_sides():
    rect.sides = (2, 2)
    assert rect.sides == (2, 2)

def test_square_type():
    assert rect.rect_type == RectangleType.square

def test_square_perimeter():
    assert rect.perimeter() == 4

def test_square_area():
    assert rect.area() == 4

def test_square_type():
    assert rect.rect_type == RectangleType.SQUARE
