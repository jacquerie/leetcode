# -*- coding: utf-8 -*-


class MyCircularDeque:
    def __init__(self, k):
        self.capacity = k
        self.count = 0
        self.elements = [0] * k
        self.index = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.index = (self.index - 1) % self.capacity
        self.elements[self.index] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.elements[(self.index + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.index = (self.index + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.elements[self.index]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.elements[(self.index + self.count - 1) % self.capacity]

    def isEmpty(self):
        return 0 == self.count

    def isFull(self):
        return self.capacity == self.count


if __name__ == '__main__':
    obj = MyCircularDeque(3)

    assert obj.insertLast(1)
    assert obj.insertLast(2)
    assert obj.insertFront(3)
    assert not obj.insertFront(4)
    assert 2 == obj.getRear()
    assert obj.isFull()
    assert obj.deleteLast()
    assert obj.insertFront(4)
    assert 4 == obj.getFront()
