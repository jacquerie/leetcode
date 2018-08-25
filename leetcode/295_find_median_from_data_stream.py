# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from heapq import heappop, heappush


class MaxHeap(object):
    def __init__(self):
        self.count = 0
        self.els = []

    def __len__(self):
        return self.count

    def _max(self):
        _, el = self.els[0]
        return el

    def pop(self):
        self.count -= 1
        _, el = heappop(self.els)
        return el

    def push(self, el):
        self.count += 1
        heappush(self.els, (-el, el))


class MinHeap(object):
    def __init__(self):
        self.count = 0
        self.els = []

    def __len__(self):
        return self.count

    def _min(self):
        return self.els[0]

    def pop(self):
        self.count -= 1
        return heappop(self.els)

    def push(self, el):
        self.count += 1
        heappush(self.els, el)


class MedianFinder(object):
    def __init__(self):
        self.small = MaxHeap()
        self.big = MinHeap()

    def addNum(self, num):
        if len(self.small) == 0 or num > self.big._min():
            self.big.push(num)
            if len(self.big) > len(self.small) + 1:
                self.small.push(self.big.pop())
        else:
            self.small.push(num)
            if len(self.small) > len(self.big):
                self.big.push(self.small.pop())

    def findMedian(self):
        if len(self.small) == len(self.big):
            return (self.small._max() + self.big._min()) / 2.0
        return self.big._min()


if __name__ == '__main__':
    obj = MedianFinder()

    obj.addNum(1)
    obj.addNum(2)
    assert 1.5 == obj.findMedian()
    obj.addNum(3)
    assert 2 == obj.findMedian()

    obj = MedianFinder()

    obj.addNum(1)
    assert 1 == obj.findMedian()

    obj = MedianFinder()

    obj.addNum(-1)
    assert -1 == obj.findMedian()
    obj.addNum(-2)
    assert -1.5 == obj.findMedian()
    obj.addNum(-3)
    assert -2 == obj.findMedian()
    obj.addNum(-4)
    assert -2.5 == obj.findMedian()
    obj.addNum(-5)
    assert -3 == obj.findMedian()
