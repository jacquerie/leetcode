# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and self.areLettersEqualButDifferentCase(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    def areLettersEqualButDifferentCase(self, char1: str, char2: str) -> bool:
        return abs(ord(char1) - ord(char2)) == 32


if __name__ == '__main__':
    solution = Solution()

    assert 'leetcode' == solution.makeGood('leEeetcode')
    assert '' == solution.makeGood('abBAcC')
    assert 's' == solution.makeGood('s')
