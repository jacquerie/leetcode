# -*- coding: utf-8 -*-


class Solution:
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            if 0 <= nums[i] - 1 < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i, num in enumerate(nums, 1):
            if i != num:
                return i
        return len(nums) + 1


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.firstMissingPositive([1, 2, 0])
    assert 2 == solution.firstMissingPositive([3, 4, -1, 1])
    assert 1 == solution.firstMissingPositive([7, 8, 9, 11, 12])
