# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        target_sum, possible_sums = sum_nums // 2, set([0])

        for num in nums:
            next_possible_sums = set()
            for possible_sum in possible_sums:
                if possible_sum + num == target_sum:
                    return True
                next_possible_sums.add(possible_sum + num)
                next_possible_sums.add(possible_sum)
            possible_sums = next_possible_sums

        return target_sum in possible_sums


if __name__ == '__main__':
    solution = Solution()

    assert solution.canPartition([1, 5, 11, 5])
    assert not solution.canPartition([1, 2, 3, 5])
