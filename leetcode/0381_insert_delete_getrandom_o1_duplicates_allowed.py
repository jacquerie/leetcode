# -*- coding: utf-8 -*-

import random
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        self.indices = defaultdict(list)
        self.elements = []
        self.length = 0

    def insert(self, val):
        result = True
        if val in self.indices:
            result = False
        self.elements.append(val)
        self.indices[val].append(self.length)
        self.length += 1
        return result

    def remove(self, val):
        result = False
        if val in self.indices:
            result = True
            index = self.indices[val].pop()
            if not self.indices[val]:
                del self.indices[val]
            self.elements[index] = None
        return result

    def getRandom(self):
        result = random.choice(self.elements)
        while result is None:
            result = random.choice(self.elements)
        return result


if __name__ == "__main__":
    obj = RandomizedCollection()

    assert obj.insert(1)
    assert not obj.insert(1)
    assert obj.insert(2)
    assert obj.getRandom() in [1, 2]
    assert obj.remove(1)
    assert obj.getRandom() in [1, 2]
