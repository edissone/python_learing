from datetime import date


def test_desktop_name(desktop_app):
    assert desktop_app.name == "Chrome"


def test_desktop_release_date(desktop_app):
    assert desktop_app.release_date == date.fromisoformat("2001-04-20")


def test_desktop_version(desktop_app):
    assert desktop_app.version == [2, 53]


def test_desktop_platform(desktop_app, desktop_platform):
    assert desktop_app.platform == desktop_platform

def test_desktop_desc(desktop_app):
    with open("res/descriptions/description.txt") as fp:
        description = fp.read()
    desktop_app.description = description

    assert desktop_app.description == description

