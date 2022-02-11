# -*- coding: utf-8 -*-

import itertools
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(
            abs(x - y) <= a and abs(y - z) <= b and abs(x - z) <= c
            for x, y, z in itertools.combinations(arr, 3)
        )


if __name__ == "__main__":
    solution = Solution()

    assert 4 == solution.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)
    assert 0 == solution.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1)
