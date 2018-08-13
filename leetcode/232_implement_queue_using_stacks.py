# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class MyQueue(object):
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.peek()
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    obj = MyQueue()

    obj.push(1)
    obj.push(2)
    assert 1 == obj.peek()
    assert 1 == obj.pop()
    assert not obj.empty()
