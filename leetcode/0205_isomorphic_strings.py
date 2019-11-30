# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution:
    def toOccurrences(self, s):
        result = defaultdict(list)

        for i, c in enumerate(s):
            result[c].append(i)

        return result.values()

    def isIsomorphic(self, s, t):
        return sorted(self.toOccurrences(s)) == sorted(self.toOccurrences(t))


if __name__ == '__main__':
    solution = Solution()

    assert solution.isIsomorphic('egg', 'add')
    assert not solution.isIsomorphic('foo', 'bar')
    assert solution.isIsomorphic('paper', 'title')
