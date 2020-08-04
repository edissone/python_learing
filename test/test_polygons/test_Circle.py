from polygons.Circle import Circle

circle = Circle(2)

def test_circle_radius():
    assert circle.radius == 2

def test_circle_area():
    assert round(circle.area()) == 13