# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counts1, counts2 = Counter(word1), Counter(word2)
        return self._check(counts1, counts2) and self._check(counts2, counts1)

    def _check(self, counts1: dict, counts2: dict) -> bool:
        for char, count in counts1.items():
            if char in counts2 and abs(count - counts2[char]) > 3:
                return False
            if char not in counts2 and count > 3:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    assert not solution.checkAlmostEquivalent("aaaa", "bccb")
    assert solution.checkAlmostEquivalent("abcdeef", "abaaacc")
    assert solution.checkAlmostEquivalent("cccddabba", "babababab")
