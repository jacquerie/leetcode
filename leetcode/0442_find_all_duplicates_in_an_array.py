# -*- coding: utf-8 -*-


class Solution:
    def findDuplicates(self, nums):
        result = []

        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]
            else:
                result.append(abs(num))

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2] == solution.findDuplicates([1, 1, 2, 3, 2])
    assert [2, 3] == solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
