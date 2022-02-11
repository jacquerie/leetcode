# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram")
    assert not solution.isAnagram("rat", "car")
