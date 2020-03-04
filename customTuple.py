"""
Task 1
Как известно, мы не всегда можем использовать tuple в качестве ключа словаря, т.к. он может включать в себя нехэшируемые
объекты. Задание - написать свою реализацию tuple, которая решает эту проблему. Лучше решать с помощью collections.abc.
Реализация хэш-функции может быть любой, лишь бы работала.
"""

from collections.abc import Hashable, Sequence
from typing import Any


class CustomTuple(Sequence, Hashable):
    def __init__(self, *elements):
        self.data = tuple(elements)

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f'{self.data}'

    def __hash__(self):
        return super().__hash__()

    def count(self, x: Any) -> int:
        c = 0
        if x in self.data:
            c += 1
        return c

    def index(self, x: Any, start: int = ..., end: int = ...) -> int:
        for i in range(start, end):
            if x == self.data[i]:
                return i
