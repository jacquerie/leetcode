# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def isValid(self, s):
        stack = deque()

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == ')' or c == ']' or c == '}':
                try:
                    top = stack.pop()
                    if top != c:
                        return False
                except IndexError:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    assert solution.isValid('()')
    assert solution.isValid('()[]{}')
    assert not solution.isValid('(]')
    assert not solution.isValid('([)]')
    assert solution.isValid('{[]}')
    assert not solution.isValid(']')
    assert not solution.isValid('[')
