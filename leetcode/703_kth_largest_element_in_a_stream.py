# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])

    assert 4 == obj.add(3)
    assert 5 == obj.add(5)
    assert 5 == obj.add(10)
    assert 8 == obj.add(9)
    assert 8 == obj.add(4)
