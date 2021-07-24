# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word1 in words:
            for word2 in words:
                if word1 in word2 and word1 != word2:
                    result.append(word1)
                    break
        return result


if __name__ == '__main__':
    solution = Solution()

    assert ['as', 'hero'] == solution.stringMatching(['mass', 'as', 'hero', 'superhero'])
    assert ['et', 'code'] == solution.stringMatching(['leetcode', 'et', 'code'])
    assert [] == solution.stringMatching(['blue', 'green', 'bu'])
