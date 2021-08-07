# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(l <= el <= r for l, r in ranges) for el in range(left, right + 1))


if __name__ == '__main__':
    solution = Solution()

    assert solution.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5)
    assert not solution.isCovered([[1, 10], [10, 20]], 21, 21)
