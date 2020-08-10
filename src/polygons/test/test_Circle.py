from src.polygons.Circle import Circle


def test_circle_radius():
    # setup
    circle = Circle(2)

    # assertion
    assert circle.radius == 2


def test_circle_area():
    # setup
    circle = Circle(2)

    # assertion
    assert circle.area == 12.566370614359172
