# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = Counter(arr)
        return self.allDistinct(counts.values())

    def allDistinct(self, arr):
        return len(arr) == len(set(arr))


if __name__ == '__main__':
    solution = Solution()

    assert solution.uniqueOccurrences([1, 2, 2, 1, 1, 3])
    assert not solution.uniqueOccurrences([1, 2])
    assert solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
