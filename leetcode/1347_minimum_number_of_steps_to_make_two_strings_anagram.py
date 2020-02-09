# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minSteps('bab', 'aba')
    assert 5 == solution.minSteps('leetcode', 'practice')
    assert 0 == solution.minSteps('anagram', 'mangaar')
    assert 0 == solution.minSteps('xxyyzz', 'xxyyzz')
    assert 4 == solution.minSteps('friend', 'family')
