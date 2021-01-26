# -*- coding: utf-8 -*-

import itertools
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(itertools.accumulate(gain)))


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.largestAltitude([-5, 1, 5, 0, -7])
    assert 0 == solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2])
