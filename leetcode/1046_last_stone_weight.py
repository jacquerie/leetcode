# -*- coding: utf-8 -*-

from heapq import heappop, heappush


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
    def lastStoneWeight(self, stones):
        heap = MaxHeap()
        for stone in stones:
            heap.push(stone)

        while len(heap) > 1:
            x = heap.pop()
            y = heap.pop()
            if x > y:
                heap.push(x - y)

        return heap.pop() if len(heap) == 1 else 0


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
    assert 0 == solution.lastStoneWeight([2, 2])
