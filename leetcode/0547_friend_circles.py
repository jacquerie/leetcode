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
    def findCircleNum(self, M):
        union_find = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] and not union_find.find(i, j):
                    union_find.union(i, j)

        return len({union_find.root(i) for i in range(len(M))})


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findCircleNum([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ])
    assert 1 == solution.findCircleNum([
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
    ])
    assert 1 == solution.findCircleNum([
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
    ])
