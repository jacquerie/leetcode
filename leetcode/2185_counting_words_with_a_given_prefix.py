# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.prefixCount(["pay", "attention", "practice", "attend"], "at")
    assert 0 == solution.prefixCount(["leetcode", "win", "loops", "success"], "code")
