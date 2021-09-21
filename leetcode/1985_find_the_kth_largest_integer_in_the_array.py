# -*- coding: utf-8 -*-

from heapq import heappop, heappush
from typing import List


class FiniteMinHeap:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.els = []

    def __len__(self) -> int:
        return self.count

    def _min(self) -> int:
        return self.els[0]

    def push(self, el: int):
        if self.count < self.capacity:
            self.count += 1
            heappush(self.els, el)
        elif el >= self._min():
            heappop(self.els)
            heappush(self.els, el)


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = FiniteMinHeap(k)
        for num in nums:
            heap.push(int(num))
        return str(heap._min())


if __name__ == '__main__':
    solution = Solution()

    assert '3' == solution.kthLargestNumber(['3', '6', '7', '10'], 4)
    assert '2' == solution.kthLargestNumber(['2', '21', '12', '1'], 3)
    assert '0' == solution.kthLargestNumber(['0', '0'], 2)
