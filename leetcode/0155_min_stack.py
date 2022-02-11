# -*- coding: utf-8 -*-

from collections import deque


class MinStack:
    def __init__(self):
        self.mins = deque()
        self.stack = deque()

    def push(self, x):
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
        self.stack.append(x - self.mins[-1])

    def pop(self):
        if not self.stack[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self):
        return self.mins[-1] + self.stack[-1]

    def getMin(self):
        return self.mins[-1]


if __name__ == "__main__":
    obj = MinStack()

    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert -3 == obj.getMin()
    obj.pop()
    assert 0 == obj.top()
    assert -2 == obj.getMin()

    obj = MinStack()

    obj.push(0)
    obj.push(1)
    obj.push(0)
    assert 0 == obj.getMin()
    obj.pop()
    assert 0 == obj.getMin()
