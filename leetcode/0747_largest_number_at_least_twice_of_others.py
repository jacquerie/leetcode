# -*- coding: utf-8 -*-


class Solution(object):
    def dominantIndex(self, nums):
        max_num = max(nums)

        for num in nums:
            if 2 * num > max_num and num != max_num:
                return -1

        return nums.index(max_num)


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.dominantIndex([3, 6, 1, 0])
    assert -1 == solution.dominantIndex([1, 2, 3, 4])
