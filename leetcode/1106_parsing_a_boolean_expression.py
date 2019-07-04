# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class Solution(object):
    def parseBoolExpr(self, expression):
        stack = deque()
        for char in expression:
            if char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char in ('!', '|', '&'):
                stack.append(char)
            elif char == ')':
                values = []
                while stack[-1] not in ('!', '|', '&'):
                    values.append(stack.pop())
                operation = stack.pop()
                result = self.evalBoolExpr(operation, values)
                stack.append(result)
        return stack[-1]

    def evalBoolExpr(self, operation, values):
        if operation == '!':
            return not values[0]
        elif operation == '|':
            return any(values)
        elif operation == '&':
            return all(values)


if __name__ == '__main__':
    solution = Solution()

    assert solution.parseBoolExpr('!(f)')
    assert solution.parseBoolExpr('|(t,f)')
    assert not solution.parseBoolExpr('&(t,f)')
    assert not solution.parseBoolExpr('|(&(t,f,t),!(t))')
