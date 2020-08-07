from src.polygons.Rectangle import *

def test_rectangle_sides(rect):
    assert rect.sides == (2, 4)

def test_rectangle_type(rect):
    assert rect.rect_type == RectangleType.RECTANGLE

def test_rectangle_perimeter(rect):
    assert rect.perimeter == 6

def test_rectangle_area(rect):
    assert rect.area == 8

def test_square_sides(square):
    assert square.sides == (2, 2)

def test_square_type(square):
    assert square.rect_type == RectangleType.SQUARE

def test_square_perimeter(square):
    assert square.perimeter == 4

def test_square_area(square):
    assert square.area == 4

