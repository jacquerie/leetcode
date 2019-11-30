# -*- coding: utf-8 -*-

from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.appendleft(x)
        for _ in range(len(self.queue) - 1):
            self.queue.appendleft(self.queue.pop())

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue[-1]

    def empty(self):
        return not self.queue


if __name__ == '__main__':
    obj = MyStack()

    obj.push(1)
    obj.push(2)
    assert 2 == obj.top()
    assert 2 == obj.pop()
    assert not obj.empty()
