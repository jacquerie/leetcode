# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def maxArea(self, height):
        i, j, result = 0, len(height) - 1, 0

        while i < j:
            result = max(result, min(height[i], height[j]) * (j - i))

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 49 == solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
