# -*- coding: utf-8 -*-


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        return [j + 1 for j, num in enumerate(nums) if num > 0]


if __name__ == '__main__':
    solution = Solution()

    assert [5, 6] == solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
