# -*- coding: utf-8 -*-

from heapq import heappop, heappush
from typing import List


class MaxHeap:
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


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        heap = MaxHeap()
        for el in cost:
            heap.push(el)

        result = 0

        while len(heap) >= 3:
            result += heap.pop()
            result += heap.pop()
            heap.pop()

        while heap:
            result += heap.pop()

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 5 == solution.minimumCost([1, 2, 3])
    assert 23 == solution.minimumCost([6, 5, 7, 9, 2, 2])
    assert 10 == solution.minimumCost([5, 5])
