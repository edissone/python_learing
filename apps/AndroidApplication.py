from datetime import date
from apps import Application, JSONSeralizable
from enum import Enum

class AndroidVersion(Enum):
    ANDROID_4_3 = "Jelly Bean 4.3"
    ANDROID_4_4 = "KitKat 4.4"
    ANDROID_5_0 = "Lollipop 5.0 "
    ANDROID_6_0 = "Marshmallow 6.0"
    ANDROID_7_0 = "Nougat 7.0"
    ANDROID_8_0 = "Oreo 8.0"
    ANDROID_9_0 = "Pie 9.0"
    ANDROID_10_0 = "Android 10"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self._name_}={self.value}"

    @classmethod
    def get_from(cls, from_index: int):
        if not isinstance(from_index, int):
            raise AttributeError("Invalid attribute")
        if not -7 < from_index < 7:
            raise IndexError("Invalid index, use -> [0:7]")
        return list(cls.__members__.values())[from_index:]


class AndroidApplication(Application.Application, JSONSeralizable.JSONSerializable):
    __slots__ = '_link', '_android_versions'

    def __init__(self, name: str, release_date: date, version: str, android_versions: list):
        if not isinstance(android_versions, list):
            raise AttributeError("Invalid attribute")
        super().__init__(name, release_date, version)
        self._android_versions = android_versions
        self._link = f"https://play.google.com/store/apps/details?id=com" \
                     f".{self._name.lower()}.{self._version}&android&hl=ru/"

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._desc}," \
               f" link={self._link}," \
               f" android_versions={self._android_versions})>"

    @property
    def link(self):
        return self.link

    @property
    def android_versions(self):
        return self._android_versions

    @android_versions.setter
    def android_versions(self, value: list):
        if not isinstance(value, list):
            raise AttributeError("Invalid attribute")
        self._android_versions = value

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
                    values_dict.update({i: value_loop})
                    i += 1
                value = values_dict
            else:
                value = getattr(self, prop)
            result.update({prop: value})
        return {self.__class__.__name__: result}

    def to_json(self):
        return super().to_json(self.to_dict())

    def write_to_json(self, path: str):
        super().write_to_json(self.to_dict(), path)
