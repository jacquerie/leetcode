# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ''

    def isPalindrome(self, word: str) -> bool:
        return word == word[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert 'ada' == solution.firstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool'])
    assert 'racecar' == solution.firstPalindrome(['notapalindrome', 'racecar'])
    assert '' == solution.firstPalindrome(['def', 'ghi'])
