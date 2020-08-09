from datetime import date
from src.apps.Application import Application
from src.apps.JSONSeralizable import JSONSerializable
from src.apps.Platform import Platform
from src.apps.exceptions.PlatformError import PlatformError

class AndroidApplication(Application, JSONSerializable):
    __slots__ = '_link', '_platform'

    def __init__(self, name: str, release_date: date, version: str, platform: Platform):
        if not isinstance(platform, Platform):
            raise AttributeError("Invalid attribute")
        if platform.device != "android" and platform.device != "cross-platform":
            raise PlatformError("This application isn't support this platform")
        super().__init__(name, release_date, version)
        self._platform = platform
        link_name = ""
        for item in name.split(" "):
            link_name += f"{item}_"
        self._link = f"https://play.google.com/store/apps/details?id=com" \
                     f".{link_name.lower()[:-1]}.{version}&android&hl=ru/"

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._description}," \
               f" link={self._link}," \
               f" platform={self._platform})>"

    @property
    def link(self):
        return self._link

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value: list):
        if not isinstance(value, list):
            raise AttributeError("Invalid attribute")
        self._platform = value

    def to_json(self):
        return super().to_json(self, super().__slots__ + self.__slots__)

    def write_to_json(self, path: str):
        super().write_to_json(self, super().__slots__ + self.__slots__, path)
