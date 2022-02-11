# -*- coding: utf-8 -*-


class UnionFind:
    def __init__(self, n):
        self.ids = list(range(n))
        self.sizes = [1] * n

    def root(self, i):
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def union(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sizes[i] < self.sizes[j]:
            self.ids[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.ids[j] = i
            self.sizes[i] += self.sizes[j]

    def find(self, p, q):
        return self.root(p) == self.root(q)


class Solution:
    def findRedundantConnection(self, edges):
        n = float("-inf")
        for u, v in edges:
            n = max(n, u, v)

        result = []

        union_find = UnionFind(n)
        for u, v in edges:
            if union_find.find(u - 1, v - 1):
                result = [u, v]
            union_find.union(u - 1, v - 1)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert [2, 3] == solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]])
    assert [1, 4] == solution.findRedundantConnection(
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    )
    assert [5, 25] == solution.findRedundantConnection(
        [
            [6, 13],
            [15, 22],
            [10, 13],
            [12, 24],
            [3, 23],
            [19, 20],
            [3, 12],
            [2, 16],
            [19, 23],
            [2, 11],
            [18, 23],
            [1, 25],
            [2, 17],
            [4, 5],
            [14, 19],
            [2, 3],
            [1, 7],
            [4, 6],
            [9, 10],
            [8, 22],
            [7, 22],
            [13, 18],
            [13, 21],
            [15, 23],
            [5, 25],
        ]
    )
