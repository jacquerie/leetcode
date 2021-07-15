# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter()
        for word in words:
            counts.update(word)

        return all(count % len(words) == 0 for count in counts.values())


if __name__ == '__main__':
    solution = Solution()

    assert solution.makeEqual(['abc', 'aabc', 'bc'])
    assert not solution.makeEqual(['ab', 'a'])
