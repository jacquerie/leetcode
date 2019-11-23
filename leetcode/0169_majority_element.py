# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        return Counter(nums).most_common(1)[0][0]


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.majorityElement([1])
    assert 1 == solution.majorityElement([1, 1, 2])
