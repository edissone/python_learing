class Arithmetic:
    MULTIPLIER = 0.5

    def __init__(self, x: int, y: int):
        if not isinstance(x, int) and not isinstance(y, int):
            raise TypeError("Type of the arguments have to be an integer")
        self._x = x
        self._y = y

    def div(self):
        return self._x / self._y

    @classmethod
    def multiply(cls, x: int):
        return cls.MULTIPLIER * x

    @staticmethod
    def operations(is_add: bool, a: int, b: int):
        if is_add:
            result = a + b
        else:
            result = b - a
        return result

    @property
    def values(self):
        return self._x, self._y

    @values.setter
    def values(self, values: tuple):
        if not len(values) == 2:
            raise ValueError("Tuple have to contain 2 args")
        self.x, self.y = values

if __name__ == "__main__":
    arithmetic = Arithmetic(10, 5)

    print(f"Values: {arithmetic.values}")
    print(f"Division: {arithmetic.div()}")
    print(f"Multiply: {Arithmetic.multiply(24)}")
    print(f"Operations(False): {Arithmetic.operations(False, 100, 40)}")
    print(f"Operations(True): {arithmetic.operations(True, 100, 40)}")

    another_values = (5, 12)
    arithmetic.values = another_values
    print(f"Values: {arithmetic.values}")
