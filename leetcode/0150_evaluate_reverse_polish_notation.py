# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def evalRPN(self, tokens):
        stack = deque()

        for token in tokens:
            if token == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif token == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif token == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif token == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / float(op2)))
            else:
                stack.append(int(token))

        return stack[-1]


if __name__ == '__main__':
    solution = Solution()

    assert 9 == solution.evalRPN(['2', '1', '+', '3', '*'])
    assert 6 == solution.evalRPN(['4', '13', '5', '/', '+'])
    assert 22 == solution.evalRPN([
        '10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
