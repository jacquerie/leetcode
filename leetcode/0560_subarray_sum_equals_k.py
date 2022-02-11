# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def subarraySum(self, nums, k):
        result = 0

        cumsum, counter = 0, Counter([0])
        for num in nums:
            cumsum += num
            result += counter[cumsum - k]
            counter[cumsum] += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.subarraySum([1, 1, 1], 2)
