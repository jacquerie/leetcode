# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        result = 0

        counter = Counter(nums)
        for num in counter:
            if num + 1 in counter:
                result = max(result, counter[num] + counter[num + 1])

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    assert 0 == solution.findLHS([1, 1, 1, 1])
