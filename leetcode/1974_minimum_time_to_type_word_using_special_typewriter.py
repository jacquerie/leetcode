# -*- coding: utf-8 -*-

class Solution:
    def minTimeToType(self, word: str) -> int:
        current_char, result = 'a', 0
        for char in word:
            current_char, result = char, result + self.timeToMove(current_char, char) + 1
        return result

    def timeToMove(self, char1, char2) -> int:
        diff = abs(ord(char1) - ord(char2))
        return min(diff, 26 - diff)


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.minTimeToType('abc')
    assert 7 == solution.minTimeToType('bza')
    assert 34 == solution.minTimeToType('zjpc')
