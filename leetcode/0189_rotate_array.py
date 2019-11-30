# -*- coding: utf-8 -*-


class Solution:
    def rotate(self, nums, k):
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]

    assert solution.rotate(nums, 3) is None
    assert [5, 6, 7, 1, 2, 3, 4] == nums
