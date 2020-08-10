from abc import ABC, abstractmethod
from datetime import date


class Application(ABC):
    __slots__ = ('_name', '_release_date', '_version', '_description')

    def __init__(self, name: str, release_date: date, version: str):
        if not isinstance(name, str) \
                or not isinstance(release_date, date) \
                or not isinstance(version, str):
            raise AttributeError("Invalid attribute")
        self._name = name
        self._release_date = release_date
        self._version = [int(item) for item in version.split(".")]
        self._description = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise AttributeError("Invalid attribute")
        self._name = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value: date):
        if not isinstance(value, date):
            raise AttributeError("Invalid attribute")
        self._release_date = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if not isinstance(value, str) and not isinstance(value, list):
            raise AttributeError("Invalid attribute")
        if isinstance(value, str):
            value = value.split(".")
            value = [int(item) for item in value]
        self._version = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise AttributeError("Invalid attribute")
        self._description = value

    def short_desc(self):
        result = ""
        sh_desc = self._description.split()
        for string in sh_desc[:50]:
            result += string.join(" ")
        return result

    def __str__(self):
        return f"Application {self._name} {self._version}, released {self._release_date}"

    @abstractmethod
    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(name={self._name},"
            f" release_date={self._release_date},"
            f" version={self._version},"
            f" desc={self.description})>"
        )

    def __eq__(self, other):
        if not isinstance(other, Application):
            raise TypeError("Attribute must be the same")

        result = True

        if self.release_date != other.release_date:
            result = self.version == other.version
        return result

    def __gt__(self, other):
        if not isinstance(other, Application):
            raise TypeError("Attribute must be the same")
        result = True

        if self.release_date == other.release_date:
            result = self.version > other.version
        return result

    def __lt__(self, other):
        if not isinstance(other, Application):
            raise TypeError("Attribute must be the same")
        return not self.__gt__(other)
