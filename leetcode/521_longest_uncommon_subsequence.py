# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.findLUSlength('aba', 'cdc')
