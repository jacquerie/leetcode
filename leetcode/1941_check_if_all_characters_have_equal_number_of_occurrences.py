# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.areOccurrencesEqual("abcabc")
    assert not solution.areOccurrencesEqual("aaabb")
