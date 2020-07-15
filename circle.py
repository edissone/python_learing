from typing import Sequence;


class CircleIterator:

    def __init__(self, sequence: Sequence, length: int):
        self._seq, self._length, self._pos = sequence, length, 0

    def __next__(self):
        if self._pos == self._length:
            raise StopIteration

        result = self._seq[self._pos % len(self._seq)]
        self._pos += 1

        return result

class Circle:

    def __init__(self, sequence: Sequence, length: int):
        self._seq = sequence
        self._length = length

    def __iter__(self):
        return CircleIterator(self._seq, self._length)

    def __len__(self):
        return self._length


if __name__ == '__main__':
    example = Circle('pyton edik', 15)
    print(list(example))
