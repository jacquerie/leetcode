# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


if __name__ == '__main__':
    solution = Solution()

    assert 6 == solution.maximumWealth([
        [1, 2, 3],
        [3, 2, 1],
    ])
    assert 10 == solution.maximumWealth([
        [1, 5],
        [7, 3],
        [3, 5],
    ])
    assert 17 == solution.maximumWealth([
        [2, 8, 7],
        [7, 1, 3],
        [1, 9, 5],
    ])
