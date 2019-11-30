# -*- coding: utf-8 -*-


class Solution:
    def maxProduct(self, nums):
        best_max, current_max, current_min = float('-inf'), 1, 1
        for num in nums:
            current_max, current_min = max(current_min * num, num, current_max * num),\
                min(current_min * num, num, current_max * num)
            best_max = max(best_max, current_max)
        return best_max


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.maxProduct([2, 3, -2, 4])
    assert 0 == solution.maxProduct([-2, 0, -1])
