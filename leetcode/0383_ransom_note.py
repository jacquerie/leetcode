# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):
        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)
        magazine_counter.subtract(ransomNote_counter)

        return all(el >= 0 for el in magazine_counter.values())


if __name__ == '__main__':
    solution = Solution()

    assert not solution.canConstruct('a', 'b')
    assert not solution.canConstruct('aa', 'ab')
    assert solution.canConstruct('aa', 'aab')
