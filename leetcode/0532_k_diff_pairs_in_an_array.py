# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        elif k == 0:
            return len([_ for _, count in Counter(nums).items() if count > 1])

        result = 0

        nums_set = set(nums)
        for num in nums_set:
            if num + k in nums_set:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findPairs([3, 1, 4, 1, 5], 2)
    assert 4 == solution.findPairs([1, 2, 3, 4, 5], 1)
    assert 1 == solution.findPairs([1, 3, 1, 5, 4], 0)
