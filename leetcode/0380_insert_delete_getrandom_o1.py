# -*- coding: utf-8 -*-

import random


class RandomizedSet(object):
    def __init__(self):
        self.indices = {}
        self.elements = []
        self.length = 0

    def insert(self, val):
        if val in self.indices:
            return False
        self.elements.append(val)
        self.indices[val] = self.length
        self.length += 1
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        self.elements[self.indices[val]] = None
        del self.indices[val]
        return True

    def getRandom(self):
        result = random.choice(self.elements)
        while result is None:
            result = random.choice(self.elements)
        return result


if __name__ == '__main__':
    obj = RandomizedSet()

    assert obj.insert(1)
    assert not obj.remove(2)
    assert obj.insert(2)
    assert obj.getRandom() in [1, 2]
    assert obj.remove(1)
    assert not obj.insert(2)
    assert 2 == obj.getRandom()
