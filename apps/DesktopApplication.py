from datetime import date
from apps import Application

class DesktopApplication(Application.Application):
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
