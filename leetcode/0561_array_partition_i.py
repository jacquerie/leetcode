# -*- coding: utf-8 -*-


class Solution(object):
    def arrayPairSum(self, nums):
        return sum(n for i, n in enumerate(sorted(nums)) if i % 2 == 0)


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.arrayPairSum([1, 4, 3, 2])
