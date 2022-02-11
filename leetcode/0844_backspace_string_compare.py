# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def backspaceCompare(self, s, t):
        return self.stringToStack(s) == self.stringToStack(t)

    def stringToStack(self, s):
        stack = deque()

        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return stack


if __name__ == "__main__":
    solution = Solution()

    assert solution.backspaceCompare("ab#c", "ad#c")
    assert solution.backspaceCompare("ab##", "c#d#")
    assert solution.backspaceCompare("a##c", "#a#c")
    assert not solution.backspaceCompare("a#c", "b")
