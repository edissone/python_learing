from src.apps.Application import Application

def test_desktop_application_inheritance(desktop_app):
    assert isinstance(desktop_app, Application)


def test_ios_application_inheritance(ios_app):
    assert isinstance(ios_app, Application)


def test_android_application_inheritance(android_app):
    assert isinstance(android_app, Application)


def test_application_versions_is_equal(desktop_app_eq_version, ios_app_eq_version):
    assert desktop_app_eq_version == ios_app_eq_version


def test_application_versions_is_not_equal(desktop_app, ios_app):
    assert desktop_app != ios_app


def test_application_versions_greater_than(desktop_app, android_app):
    assert desktop_app > android_app

def test_application_versions_not_greater(desktop_app, android_app):
    assert not desktop_app < android_app

def test_application_versions_less_than(ios_app, android_app):
    assert ios_app > android_app

def test_application_versions_not_less_than(ios_app, android_app):
    assert not ios_app < android_app


