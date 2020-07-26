# -*- coding: utf-8 -*-


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.countOdds(3, 7)
    assert 1 == solution.countOdds(8, 10)
