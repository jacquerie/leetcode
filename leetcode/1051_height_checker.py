# -*- coding: utf-8 -*-


class Solution:
    def heightChecker(self, heights):
        return sum(x != y for x, y in zip(heights, sorted(heights)))


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.heightChecker([1, 1, 4, 2, 1, 3])
