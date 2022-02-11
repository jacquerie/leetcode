# -*- coding: utf-8 -*-

from heapq import heappop, heappush
from typing import List


class MinHeap:
    def __init__(self):
        self.els = []

    def pop(self):
        return heappop(self.els)

    def push(self, el):
        heappush(self.els, el)


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap = MinHeap()
        for el in A:
            heap.push(el)

        for _ in range(K):
            el = heap.pop()
            heap.push(-el)

        return sum(heap.els)


if __name__ == "__main__":
    solution = Solution()

    assert 5 == solution.largestSumAfterKNegations([4, 2, 3], 1)
    assert 6 == solution.largestSumAfterKNegations([3, -1, 0, 2], 3)
    assert 13 == solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2)
