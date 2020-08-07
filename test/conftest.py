import pytest
from apps.Platform import Platform
from polygons.Circle import Circle


# platform fixtures
@pytest.fixture(scope="module")
def desktop_platform():
    return Platform("Windows", 64, "desk")


@pytest.fixture(scope="module")
def cross_platform():
    return Platform("Virtual", 32, "")


# circle fixtures
@pytest.fixture(scope="module")
def circle():
    return Circle(2)
