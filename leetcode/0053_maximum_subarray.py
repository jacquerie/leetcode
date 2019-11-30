# -*- coding: utf-8 -*-


class Solution:
    def maxSubArray(self, nums):
        best_max, current_max = float('-inf'), 0
        for num in nums:
            current_max = max(num, current_max + num)
            best_max = max(best_max, current_max)
        return best_max


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
