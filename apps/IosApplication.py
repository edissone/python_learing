from datetime import date
from apps import Application, JSONSeralizable

from enum import Enum

class IOSVersion(Enum):
    IOS_4 = "iOS 4"
    IOS_5 = "iOS 5"
    IOS_6 = "iOS 6"
    IOS_7 = "iOS 7"
    IOS_8 = "iOS 8"
    IOS_9 = "iOS 9"
    IOS_10 = "iOS 10"
    IOS_11 = "iOS 11"
    IOS_12 = "iOS 12"
    IOS_13 = "iOS 13"
    IOS_14 = "iOS 14"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self._name_}={self.value}"

    @classmethod
    def get_from(cls, from_index: int):
        if not isinstance(from_index, int):
            raise AttributeError("Invalid attribute")
        if not -11 < from_index < 11:
            raise IndexError("Invalid index, use -> [-11:11]")
        return list(cls.__members__.values())[from_index:]

class IosApplication(Application.Application, JSONSeralizable.JSONSerializable):
    __slots__ = '_link', '_ios_versions'

    def __init__(self, name: str, release_date: date, version: str, ios_versions: list):
        if not isinstance(ios_versions, list):
            raise AttributeError("Invalid attribute")
        super().__init__(name, release_date, version)
        self._ios_versions = ios_versions
        self._link = f"https://apps.apple.com/ru/app/{self._name.lower()}.{self._version}/"

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._description}," \
               f" link={self._link}," \
               f" ios_versions={self._ios_versions})>"

    @property
    def link(self):
        return self._link

    @property
    def ios_versions(self):
        return self._ios_versions

    @ios_versions.setter
    def ios_versions(self, value: list):
        if not isinstance(value, list):
            raise AttributeError("Invalid attribute")
        self._ios_versions = value

    def to_dict(self):
        result = dict()
        properties = super().__slots__ + self.__slots__
        for prop in properties:
            prop = prop[1:]
            if isinstance(getattr(self, prop), list):
                values_set = getattr(self, prop)
                i = 0
                values_dict = dict()
                for value_loop in values_set:
                    values_dict.update({i: value_loop.value})
                    i += 1
                value = values_dict
            else: value = getattr(self, prop)
            result.update({prop: value})
        return {self.__class__.__name__: result}

    def to_json(self):
        return super().to_json(self.to_dict())

    def write_to_json(self, path: str):
        super().write_to_json(self.to_dict(), path)
