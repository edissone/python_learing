from datetime import date
from apps import Application

class IosApplication(Application.Application):
    __slots__ = '_link', '_ios_versions'

    def __init__(self, name: str, release_date: date, version: str, ios_versions: set):
        if not isinstance(ios_versions, set):
            raise AttributeError("Invalid attribute")
        super().__init__(name, release_date, version)
        self._ios_versions = ios_versions
        self._link = f"https://apps.apple.com/ru/app/{self._name.lower()}.{self._version}/"

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self._name}," \
               f" release_date={self._release_date}," \
               f" version={self._version}," \
               f" desc={self._desc}," \
               f" link={self._link}," \
               f" ios_versions={self._ios_versions})>"

    @property
    def link(self):
        return self.link

    @property
    def ios_versions(self):
        return self._ios_versions

    @ios_versions.setter
    def ios_versions(self, value: set):
        if not isinstance(value, set):
            raise AttributeError("Invalid attribute")
        self._ios_versions = value
