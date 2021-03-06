import pytest
from datetime import date
# apps
from src.apps.DesktopApplication import DesktopApplication
from src.apps.IosApplication import IosApplication
from src.apps.AndroidApplication import AndroidApplication
from src.apps.Platform import Platform, DEVICE
# polygons
from src.polygons.Triangle import Triangle
from src.polygons.Circle import Circle
from src.polygons.Rectangle import Rectangle


# apps:
# platform fixtures
# desktop platform fixture
@pytest.fixture()
def desktop_platform():
    return Platform("Windows", 64, DEVICE.DESKTOP)


# cross-platform fixtures
@pytest.fixture()
def cross_platform():
    return Platform("Virtual", 32, DEVICE.CROSS_PLATFORM)

# ios platform fixtures
@pytest.fixture()
def ios_platform():
    return Platform("OS X", 64, DEVICE.IOS)


# android_platform fixture
@pytest.fixture()
def android_platform():
    return Platform("Android 10", 32, DEVICE.ANDROID)


# desktop application fixtures
@pytest.fixture()
def desktop_app(desktop_platform):
    return DesktopApplication("Chrome", date.fromisoformat("2001-04-20"), "2.53", desktop_platform)


@pytest.fixture()
def desktop_app_eq_version(desktop_platform):
    return DesktopApplication("Chrome", date.fromisoformat("2007-10-31"), "1.23", desktop_platform)


# ios application fixtures
@pytest.fixture()
def ios_app(ios_platform):
    return IosApplication("App Store", date.fromisoformat("2007-10-31"), "25.7.1", ios_platform)


@pytest.fixture()
def ios_app_eq_version(ios_platform):
    return IosApplication("App Store", date.fromisoformat("2008-10-31"), "1.23", ios_platform)


@pytest.fixture()
def android_app(android_platform):
    return AndroidApplication("Play Market", date.fromisoformat("2017-01-02"), "1.0.1", android_platform)


# polygons:
# circle fixtures
@pytest.fixture()
def circle():
    return Circle(2)


# rectangle fixtures
@pytest.fixture()
def rect():
    return Rectangle((2, 4))


@pytest.fixture()
def square():
    return Rectangle((2, 2))


# triangle fixtures
@pytest.fixture()
def versatile():
    return Triangle((1, 4, 7))


@pytest.fixture()
def equilateral():
    return Triangle((3, 3, 3))


@pytest.fixture()
def rectangular():
    return Triangle((3, 4, 5))
