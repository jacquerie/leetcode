# -*- coding: utf-8 -*-


class MyHashSet(object):
    def __init__(self):
        self.data = [False] * (2 ** 20)

    def add(self, key):
        self.data[key] = True

    def contains(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = False


if __name__ == '__main__':
    obj = MyHashSet()

    obj.add(1)
    obj.add(2)
    assert obj.contains(1)
    assert not obj.contains(3)
    obj.add(2)
    assert obj.contains(2)
    obj.remove(2)
    assert not obj.contains(2)
