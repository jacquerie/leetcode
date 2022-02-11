# -*- coding: utf-8 -*-

import itertools


class Solution:
    def maxPower(self, s: str) -> int:
        result = 0
        for _, group in itertools.groupby(s):
            result = max(result, len(list(group)))
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.maxPower("leetcode")
    assert 5 == solution.maxPower("abbcccddddeeeeedcba")
    assert 5 == solution.maxPower("triplepillooooow")
    assert 11 == solution.maxPower("hooraaaaaaaaaaay")
    assert 1 == solution.maxPower("tourist")
