# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        counts = Counter(text)
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.maxNumberOfBalloons('nlaebolko')
    assert 2 == solution.maxNumberOfBalloons('loonbalxballpoon')
    assert 0 == solution.maxNumberOfBalloons('leetcode')
