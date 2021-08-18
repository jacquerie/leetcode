# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numOfStrings(['a', 'abc', 'bc', 'd'], 'abc')
    assert 2 == solution.numOfStrings(['a', 'b', 'c'], 'aaaaabbbbb')
    assert 3 == solution.numOfStrings(['a', 'a', 'a'], 'ab')
