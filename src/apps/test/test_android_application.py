from datetime import date


def test_android_name(android_app):
    assert android_app.name == "Play Market"


def test_android_release_date(android_app):
    assert android_app.release_date == date.fromisoformat("2017-01-02")


def test_android_version(android_app):
    assert android_app.version == [1, 0, 1]


def test_desktop_platform(android_app, android_platform):
    assert android_app.platform == android_platform


def test_ios_desc(android_app):
    with open("res/descriptions/description.txt") as fp:
        description = fp.read()
    android_app.description = description

    assert android_app.description == description

def test_ios_link(android_app):
    assert android_app.link == "https://play.google.com/store/apps/details?id=com.play_market.1.0.1&android&hl=ru/"
