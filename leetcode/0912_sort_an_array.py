# -*- coding: utf-8 -*-


class Solution:
    def sortArray(self, nums):
        return sorted(nums)


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2, 3, 5] == solution.sortArray([5, 2, 3, 1])
    assert [0, 0, 1, 1, 2, 5] == solution.sortArray([5, 1, 1, 2, 0, 0])
