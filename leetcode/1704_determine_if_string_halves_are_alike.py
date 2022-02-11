# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return self.countVowels(s[: len(s) // 2]) == self.countVowels(s[len(s) // 2 :])

    def countVowels(self, s: str) -> int:
        counts = Counter(s.lower())
        return counts["a"] + counts["e"] + counts["i"] + counts["o"] + counts["u"]


if __name__ == "__main__":
    solution = Solution()

    assert solution.halvesAreAlike("book")
    assert not solution.halvesAreAlike("textbook")
    assert not solution.halvesAreAlike("MerryChristmas")
    assert solution.halvesAreAlike("AbCdEfGh")
