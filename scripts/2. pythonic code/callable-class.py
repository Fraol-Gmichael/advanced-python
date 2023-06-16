from collections import defaultdict
from typing import Any


class CallCount:
    def __init__(self) -> None:
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts


cc = CallCount()

print(cc(1), cc(3), cc(1))
