# -*- coding: utf-8 -*-


class Solution:
    def smallestRangeI(self, A, K):
        minimum, maximum = self.findMinMax(A)
        return max((maximum - K) - (minimum + K), 0)

    def findMinMax(self, A):
        minimum, maximum = float('inf'), float('-inf')
        for el in A:
            minimum, maximum = min(minimum, el), max(maximum, el)
        return minimum, maximum


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.smallestRangeI([1], 0)
    assert 6 == solution.smallestRangeI([0, 10], 2)
    assert 0 == solution.smallestRangeI([1, 3, 6], 3)
