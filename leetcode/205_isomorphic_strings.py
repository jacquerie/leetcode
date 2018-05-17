# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import defaultdict


class Solution(object):
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
