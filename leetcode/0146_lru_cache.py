# -*- coding: utf-8 -*-

from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    obj = LRUCache(2)

    obj.put(1, 1)
    obj.put(2, 2)
    assert 1 == obj.get(1)
    obj.put(3, 3)
    assert -1 == obj.get(2)
    obj.put(4, 4)
    assert -1 == obj.get(1)
    assert 3 == obj.get(3)
    assert 4 == obj.get(4)
