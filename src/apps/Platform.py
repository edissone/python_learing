from src.apps.JSONSeralizable import JSONSerializable
from enum import Enum


class DEVICE(Enum):
    ANDROID = "a"
    IOS = "i"
    DESKTOP = "d"
    CROSS_PLATFORM = "c"

class Platform(JSONSerializable):
    __slots__ = "_name", "_bit_base", "_device"

    def __init__(self, name: str, bit_base: int, device: DEVICE):

        if not isinstance(name, str) or not isinstance(bit_base, int) or not isinstance(device, DEVICE):
            raise AttributeError("Invalid attribute")

        self._name = name
        if bit_base not in (32, 64):
            raise ValueError("Platform can't be x{bit_base}-based, set default value: 32")
        self._bit_base = bit_base
        self._device = device

    def __class__(self):
        return "Platform"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise AttributeError("Invalid attribute")
        self._name = value

    @property
    def bit_base(self):
        return self._bit_base

    @bit_base.setter
    def bit_base(self, value: int):
        if not isinstance(value, int):
            raise AttributeError("Invalid attribute")
        self._bit_base = value

    @property
    def device(self):
        return self._device

    @property
    def fields(self):
        return self.__slots__

    @device.setter
    def device(self, value: DEVICE):
        if not isinstance(value, DEVICE):
            raise AttributeError("Invalid attribute")
        self._device = value

    def to_json(self):
        return super().to_json(self, self.__slots__)
