# -*- coding: utf-8 -*-

from collections import deque
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = deque()

        for op in ops:
            if op == '+':
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(p1)
                stack.append(p2)
                stack.append(p1 + p2)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                p = stack.pop()
                stack.append(p)
                stack.append(2 * p)
            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == '__main__':
    solution = Solution()

    assert 30 == solution.calPoints(['5', '2', 'C', 'D', '+'])
    assert 27 == solution.calPoints(['5', '-2', '4', 'C', 'D', '9', '+', '+'])
