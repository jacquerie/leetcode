# -*- coding: utf-8 -*-


class MyHashMap(object):
    def __init__(self):
        self.data = [-1] * (2 ** 20)

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = -1


if __name__ == '__main__':
    obj = MyHashMap()

    obj.put(1, 1)
    obj.put(2, 2)
    assert 1 == obj.get(1)
    assert -1 == obj.get(3)
    obj.put(2, 1)
    assert 1 == obj.get(2)
    obj.remove(2)
    assert -1 == obj.get(2)
