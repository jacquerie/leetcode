# -*- coding: utf-8 -*-


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)


if __name__ == '__main__':
    solution = Solution()

    assert 13 == solution.numWaterBottles(9, 3)
    assert 19 == solution.numWaterBottles(15, 4)
    assert 6 == solution.numWaterBottles(5, 5)
    assert 2 == solution.numWaterBottles(2, 3)
