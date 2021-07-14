# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_count, zero_seen = 0, False
        for num in nums:
            if num == 0:
                zero_seen = True
            elif num < 0:
                negative_count += 1

        if zero_seen:
            return 0
        return 1 if negative_count % 2 == 0 else -1


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.arraySign([-1, -2, -3, -4, 3, 2, 1])
    assert 0 == solution.arraySign([1, 5, 0, 2, -3])
    assert -1 == solution.arraySign([-1, 1, -1, 1, -1])
