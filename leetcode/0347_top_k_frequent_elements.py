# -*- coding: utf-8 -*-

from collections import Counter
from heapq import heappop, heappush


class MaxHeap(object):
    def __init__(self):
        self.els = []

    def __len__(self):
        return len(self.els)

    def __nonzero__(self):
        return len(self.els) > 0

    def pop(self):
        _, el = heappop(self.els)
        return el

    def push(self, el, count):
        heappush(self.els, (count, el))


class Solution(object):
    def topKFrequent(self, nums, k):
        counter, heap = Counter(nums), MaxHeap()
        for el, count in counter.items():
            heap.push(el, count)
            if len(heap) > k:
                heap.pop()

        result = []
        while heap:
            result.append(heap.pop())
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2] == solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert [1] == solution.topKFrequent([1], 1)
