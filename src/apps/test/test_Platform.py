from src.apps.Platform import DEVICE


def test_desktop_platform_name(desktop_platform):
    assert desktop_platform.name == "Windows"


def test_desktop_platform_bit_base(desktop_platform):
    assert desktop_platform.bit_base == 64


def test_desktop_platform_device(desktop_platform):
    assert desktop_platform.device == DEVICE.DESKTOP


def test_cross_platform_name(cross_platform):
    assert cross_platform.name == "Virtual"


def test_cross_platform_bit_base(cross_platform):
    assert cross_platform.bit_base == 32


def test_cross_platform_device(cross_platform):
    assert cross_platform.device == DEVICE.CROSS_PLATFORM


def test_ios_platform_name(ios_platform):
    assert ios_platform.name == "OS X"


def test_ios_platform_bit_base(ios_platform):
    assert ios_platform.bit_base == 64


def test_ios_platform_device(ios_platform):
    assert ios_platform.device == DEVICE.IOS


def test_android_platform_name(android_platform):
    assert android_platform.name == "Android 10"


def test_android_platform_bit_base(android_platform):
    assert android_platform.bit_base == 32


def test_android_platform_device(android_platform):
    assert android_platform.device == DEVICE.ANDROID
