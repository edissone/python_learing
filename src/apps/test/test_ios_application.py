from datetime import date


def test_ios_name(ios_app):
    assert ios_app.name == "App Store"


def test_ios_release_date(ios_app):
    assert ios_app.release_date == date.fromisoformat("2007-10-31")


def test_ios_version(ios_app):
    assert ios_app.version == [25, 7, 1]


def test_desktop_platform(ios_app, ios_platform):
    assert ios_app.platform == ios_platform


def test_ios_desc(ios_app):
    with open("res/descriptions/description.txt") as fp:
        description = fp.read()
    ios_app.description = description

    assert ios_app.description == description

def test_ios_link(ios_app):
    assert ios_app.link == "https://apps.apple.com/ru/app/app_store.25.7.1/"
