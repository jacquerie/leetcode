# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counts1, counts2 = Counter(words1), Counter(words2)
        set1, set2 = self.selectElsOfCountOne(counts1), self.selectElsOfCountOne(counts2)
        return len(set1 & set2)

    def selectElsOfCountOne(self, counts: dict) -> set:
        return set(el for el, count in counts.items() if count == 1)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.countWords(['leetcode', 'is', 'amazing', 'as', 'is'], ['amazing', 'leetcode', 'is'])
    assert 0 == solution.countWords(['b', 'bb', 'bbb'], ['a', 'aa', 'aaa'])
    assert 1 == solution.countWords(['a', 'ab'], ['a', 'a', 'a', 'ab'])
