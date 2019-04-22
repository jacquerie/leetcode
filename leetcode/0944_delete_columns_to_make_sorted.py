# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minDeletionSize(self, A):
        return len([col for col in zip(*A) if col != tuple(sorted(col))])


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minDeletionSize(['cba', 'daf', 'ghi'])
    assert 0 == solution.minDeletionSize(['a', 'b'])
    assert 3 == solution.minDeletionSize(['zyx', 'wvu', 'tsr'])
