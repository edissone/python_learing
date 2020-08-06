from polygons.Rectangle import *

def test_rectangle_sides():
    # setup
    rect = Rectangle((2, 4))

    # assertion
    assert rect.sides == (2, 4)

def test_rectangle_type():
    # setup
    rect = Rectangle((2, 4))

    # assertion
    assert rect.rect_type == RectangleType.RECTANGLE

def test_rectangle_perimeter():
    # setup
    rect = Rectangle((2, 4))

    # assertion
    assert rect.perimeter == 6

def test_rectangle_area():
    # setup
    rect = Rectangle((2, 4))

    # assertion
    assert rect.area == 8

def test_square_sides():
    # setup
    rect = Rectangle((2, 2))

    # assertion
    assert rect.sides == (2, 2)

def test_square_type():
    # setup
    rect = Rectangle((2, 4))

    # assertion
    assert rect.rect_type == RectangleType.square

def test_square_perimeter():
    # setup
    rect = Rectangle((2, 2))

    # assertion
    assert rect.perimeter == 4

def test_square_area():
    # setup
    rect = Rectangle((2, 2))

    # assertion
    assert rect.area == 4

def test_square_type():
    # setup
    rect = Rectangle((2, 2))

    # assertion
    assert rect.rect_type == RectangleType.SQUARE
