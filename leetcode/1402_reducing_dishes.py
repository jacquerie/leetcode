# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        total_satisfaction_so_far, result = 0, 0

        satisfaction.sort(reverse=True)
        for el in satisfaction:
            if total_satisfaction_so_far + el <= 0:
                break
            total_satisfaction_so_far += el
            result += total_satisfaction_so_far

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 14 == solution.maxSatisfaction([-1, -8, 0, 5, -9])
    assert 20 == solution.maxSatisfaction([4, 3, 2])
    assert 0 == solution.maxSatisfaction([-1, -4, -5])
    assert 35 == solution.maxSatisfaction([-2, 5, -1, 0, 3, -3])
