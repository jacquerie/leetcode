# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def maxChunksToSorted(self, arr):
        result = 0

        current_max_i = 0
        for i, el in enumerate(arr):
            current_max_i = max(current_max_i, el)
            if i == current_max_i:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.maxChunksToSorted([4, 3, 2, 1, 0])
    assert 4 == solution.maxChunksToSorted([1, 0, 2, 3, 4])
