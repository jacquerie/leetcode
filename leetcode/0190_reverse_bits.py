# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def reverseBits(self, n):
        return int(''.join(reversed(format(n, '032b'))), 2)


if __name__ == '__main__':
    solution = Solution()

    assert 964176192 == solution.reverseBits(43261596)
