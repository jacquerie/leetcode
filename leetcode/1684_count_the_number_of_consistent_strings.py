# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(char in set(allowed) for char in word) for word in words)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.countConsistentStrings('ab', ['ad', 'bd', 'aaab', 'baa', 'badab'])
    assert 7 == solution.countConsistentStrings('abc', ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'])
    assert 4 == solution.countConsistentStrings('cad', ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd'])
