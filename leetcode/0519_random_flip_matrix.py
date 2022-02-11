# -*- coding: utf-8 -*-

import random


class Solution:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.reset()

    def flip(self):
        self.count -= 1
        index = random.randint(0, self.count)
        result = self.elements.get(index, index)
        self.elements[index] = self.elements.get(self.count, self.count)
        return divmod(result, self.n_cols)

    def reset(self):
        self.count = self.n_rows * self.n_cols
        self.elements = {}


if __name__ == "__main__":
    obj = Solution(2, 3)

    assert obj.flip() in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    assert obj.flip() in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    assert obj.flip() in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    assert obj.flip() in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    obj = Solution(1, 2)

    assert obj.flip() in [(0, 0), (0, 1)]
    assert obj.flip() in [(0, 0), (0, 1)]
    obj.reset()
    assert obj.flip() in [(0, 0), (0, 1)]
