# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def matrixReshape(self, nums, r, c):
        original_r, original_c = len(nums), len(nums[0])
        if r * c != original_r * original_c:
            return nums

        tmp = [nums[i][j] for i in xrange(original_r) for j in xrange(original_c)]

        result = []
        for i in xrange(r):
            row = []
            for j in xrange(c):
                row.append(tmp[i * c + j])
            result.append(row)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[1, 2, 3, 4]] == solution.matrixReshape([[1, 2], [3, 4]], 1, 4)
    assert [[1, 2], [3, 4]] == solution.matrixReshape([[1, 2], [3, 4]], 2, 4)
