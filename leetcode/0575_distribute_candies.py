# -*- coding: utf-8 -*-


class Solution:
    def distributeCandies(self, candies):
        return min(len(candies) / 2, len(set(candies)))


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.distributeCandies([1, 1, 2, 2, 3, 3])
    assert 2 == solution.distributeCandies([1, 1, 2, 3])
