from datetime import date
from apps import Application, JSONSeralizable

class DesktopApplication(Application.Application, JSONSeralizable.JSONSerializable):
    __slots__ = '_platforms'

    def __init__(self, name: str, release_date: date, version: str, platforms: set):
        if not isinstance(platforms, set):
            raise AttributeError("Invalid attribute")
        super().__init__(name, release_date, version)
        self._platforms = platforms

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._desc}," \
               f" platforms={self._platforms})>"

    @property
    def link(self):
        return self.link

    @property
    def platforms(self):
        return self._platforms

    @platforms.setter
    def platforms(self, value: set):
        if not isinstance(value, set):
            raise AttributeError("Invalid attribute")
        self._platforms = value

    def to_dict(self):
        result = dict()
        properties = super().__slots__ + self.__slots__
        for prop in properties:
            value = None
            prop = prop[1:]
            if isinstance(getattr(self, prop), set):
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