from datetime import date
from apps.Application import Application
from apps.JSONSeralizable import JSONSerializable
from apps.Platform import Platform
from apps.exceptions.PlatformError import PlatformError


class DesktopApplication(Application, JSONSerializable):
    __slots__ = ('_platform',)

    def __init__(self, name: str, release_date: date, version: str, platform: Platform):
        if not isinstance(platform, Platform):
            raise AttributeError("Invalid attribute")
        if platform.device != "desktop" and platform.device != "cross-platform":
            raise PlatformError("This application isn't support this platform")
        super().__init__(name, release_date, version)
        self._platform = platform

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._description}," \
               f" platform={self._platform})>"

    @property
    def link(self):
        return self.link

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value: Platform):
        if not isinstance(value, Platform):
            raise AttributeError("Invalid attribute")
        self._platform = value

    def to_json(self):
        return super().to_json(self, super().__slots__ + self.__slots__)

    def write_to_json(self, path: str):
        super().write_to_json(self, super().__slots__ + self.__slots__, path)
