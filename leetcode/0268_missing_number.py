# -*- coding: utf-8 -*-


class Solution(object):
    def missingNumber(self, nums):
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.missingNumber([3, 0, 1])
    assert 8 == solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
