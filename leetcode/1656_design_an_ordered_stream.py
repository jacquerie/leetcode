# -*- coding: utf-8 -*-

from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.els = [None] * (n + 1)
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.els[id] = value

        result = []
        if id == self.ptr:
            while self.ptr < len(self.els) and self.els[self.ptr] is not None:
                result.append(self.els[self.ptr])
                self.ptr += 1
        return result


if __name__ == "__main__":
    obj = OrderedStream(5)

    assert [] == obj.insert(3, "ccccc")
    assert ["aaaaa"] == obj.insert(1, "aaaaa")
    assert ["bbbbb", "ccccc"] == obj.insert(2, "bbbbb")
    assert [] == obj.insert(5, "eeeee")
    assert ["ddddd", "eeeee"] == obj.insert(4, "ddddd")
