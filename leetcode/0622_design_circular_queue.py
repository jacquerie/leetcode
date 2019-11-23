# -*- coding: utf-8 -*-


class MyCircularQueue(object):
    def __init__(self, k):
        self.capacity = k
        self.count = 0
        self.elements = [0] * k
        self.index = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.elements[(self.index + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.index = (self.index + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.elements[self.index]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.elements[(self.index + self.count - 1) % self.capacity]

    def isEmpty(self):
        return 0 == self.count

    def isFull(self):
        return self.capacity == self.count


if __name__ == '__main__':
    obj = MyCircularQueue(3)

    assert obj.enQueue(1)
    assert obj.enQueue(2)
    assert obj.enQueue(3)
    assert not obj.enQueue(4)
    assert 3 == obj.Rear()
    assert obj.isFull()
    assert obj.deQueue()
    assert obj.enQueue(4)
    assert 4 == obj.Rear()
