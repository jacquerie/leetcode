# -*- coding: utf-8 -*-

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.ids = list(range(n))
        self.sizes = [1] * n

    def root(self, i: int) -> int:
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def union(self, p: int, q: int):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sizes[i] < self.sizes[j]:
            self.ids[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.ids[j] = i
            self.sizes[i] += self.sizes[j]

    def find(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union(u, v)
        return union_find.find(start, end)


if __name__ == "__main__":
    solution = Solution()

    assert solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
    assert not solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
