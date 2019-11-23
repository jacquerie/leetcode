# -*- coding: utf-8 -*-

from collections import Counter, defaultdict


class FreqStack(object):
    def __init__(self):
        self.counter = Counter()
        self.elements = defaultdict(list)
        self.max_count = 0

    def push(self, x):
        self.counter[x] += 1
        if self.counter[x] > self.max_count:
            self.max_count += 1
        self.elements[self.counter[x]].append(x)

    def pop(self):
        x = self.elements[self.max_count].pop()
        self.counter[x] -= 1
        if not self.elements[self.max_count]:
            self.max_count -= 1
        return x


if __name__ == '__main__':
    obj = FreqStack()

    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    assert 5 == obj.pop()
    assert 7 == obj.pop()
    assert 5 == obj.pop()
    assert 4 == obj.pop()
