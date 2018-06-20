# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class UnionFind(object):
    def __init__(self, n):
        self.ids = list(range(n))
        self.lengths = [1] * n

    def root(self, i):
        j = i
        while (j != self.ids[j]):
            self.ids[j] = self.ids[self.ids[j]]
            j = self.ids[j]
        return j

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.lengths[i] < self.lengths[j]:
            self.ids[i] = j
            self.lengths[j] += self.lengths[i]
        else:
            self.ids[j] = i
            self.lengths[i] += self.lengths[j]


class Solution(object):
    def arrayNesting(self, nums):
        union_find = UnionFind(len(nums))
        for num in nums:
            union_find.union(num, nums[num])
        return max(union_find.lengths)


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.arrayNesting([5, 4, 0, 3, 1, 6, 2])
