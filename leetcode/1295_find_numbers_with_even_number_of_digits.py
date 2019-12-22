# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if 10 <= num < 100 or 1000 <= num < 10000:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findNumbers([12, 345, 2, 6, 7896])
    assert 1 == solution.findNumbers([555, 901, 482, 1771])
