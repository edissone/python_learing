from datetime import date
from apps import Application, JSONSeralizable
from enum import Enum
class Platforms(Enum):
    MACOS = "Mac OS"
    WIN7 = "Windows 7"
    WIN10 = "Windows 10"

    def __str__(self):
        return self.value

    @classmethod
    def get_all(cls):
        return list(cls.__members__.values())

class DesktopApplication(Application.Application, JSONSeralizable.JSONSerializable):
    __slots__ = ('_platforms',)

    def __init__(self, name: str, release_date: date, version: str, platforms: list):
        if not isinstance(platforms, list):
            raise AttributeError("Invalid attribute")
        super().__init__(name, release_date, version)
        self._platforms = platforms

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._description}," \
               f" platforms={self._platforms})>"

    @property
    def link(self):
        return self.link

    @property
    def platforms(self):
        return self._platforms

    @platforms.setter
    def platforms(self, value: list):
        if not isinstance(value, list):
            raise AttributeError("Invalid attribute")
        self._platforms = value

    def to_json(self):
        return super().to_json(self, super().__slots__ + self.__slots__)

    def write_to_json(self, path: str):
        super().write_to_json(self, super().__slots__ + self.__slots__, path)
