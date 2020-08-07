from src.apps.JSONSeralizable import JSONSerializable

class Platform(JSONSerializable):
    __slots__ = "_name", "_bit_base", "_device"

    def __init__(self, name: str, bit_base: int, device_string: str):

        if not isinstance(name, str) or not isinstance(bit_base, int) or not isinstance(device_string, str):
            raise AttributeError("Invalid attribute")
        else:
            self._name = name
            if bit_base != 64 and bit_base != 32:
                print(f"Platform can't be x{bit_base}-based, set default value: 32")
                self._bit_base = 32
            else:
                self._bit_base = bit_base
            self._device = self._identify_device(device_string)

    def __class__(self):
        return "Platform"

    @staticmethod
    def _identify_device(device_string):
        device_char = device_string[0].lower() if not device_string == "" else " "

        if device_char == "a":
            result = "android"
        elif device_char == "d":
            result = "desktop"
        elif device_char == "i":
            result = "ios"
        else:
            result = "cross-platform"

        return result

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
    def device(self, value: str):
        if not isinstance(value, str):
            raise AttributeError("Invalid attribute")
        self._name = self._identify_device(value)

    def to_json(self):
        return super().to_json(self, self.__slots__)
