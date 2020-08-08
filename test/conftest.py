import pytest
from datetime import date
# apps
from src.apps.DesktopApplication import DesktopApplication
from src.apps.Platform import Platform
# polygons
from src.polygons.Triangle import Triangle
from src.polygons.Circle import Circle
from src.polygons.Rectangle import Rectangle


# apps:
# platform fixtures
@pytest.fixture(scope="module")
def desktop_platform():
    return Platform("Windows", 64, "desk")


@pytest.fixture(scope="module")
def cross_platform():
    return Platform("Virtual", 32, "")


@pytest.fixture(scope="module")
def ios_platform():
    return Platform("OS X", 64, "I")


@pytest.fixture(scope="module")
def android_platform():
    return Platform("Android 10", 32, "Android")


# desktop application fixtures
@pytest.fixture(scope="module")
def desktop_app():
    return DesktopApplication("Chrome", date.fromisoformat("2001-04-20"), "", desktop_platform)


# polygons:
# circle fixtures
@pytest.fixture(scope="module")
def circle():
    return Circle(2)


# rectangle fixtures
@pytest.fixture(scope="module")
def rect():
    return Rectangle((2, 4))


@pytest.fixture(scope="module")
def square():
    return Rectangle((2, 2))


# triangle fixtures
@pytest.fixture(scope="module")
def versatile():
    return Triangle((1, 4, 7))


@pytest.fixture(scope="module")
def equilateral():
    return Triangle((3, 3, 3))


@pytest.fixture(scope="module")
def rectangular():
    return Triangle((3, 4, 5))
