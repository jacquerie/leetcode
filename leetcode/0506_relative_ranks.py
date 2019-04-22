# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findRelativeRanks(self, nums):
        sorted_nums = sorted(nums, reverse=True)
        ranks = {num: rank for rank, num in enumerate(sorted_nums, 1)}

        result = []

        for num in nums:
            rank = ranks[num]
            if rank > 3:
                result.append(str(rank))
            elif rank == 3:
                result.append('Bronze Medal')
            elif rank == 2:
                result.append('Silver Medal')
            elif rank == 1:
                result.append('Gold Medal')

        return result


if __name__ == '__main__':
    solution = Solution()

    assert ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5'] == solution.findRelativeRanks([5, 4, 3, 2, 1])
