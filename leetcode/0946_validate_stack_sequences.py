# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def validateStackSequences(self, pushed, popped):
        i, j, stack = 0, 0, deque()
        while i < len(pushed) or j < len(popped):
            if j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < len(pushed):
                stack.append(pushed[i])
                i += 1
            else:
                return False
        return i == len(pushed) and j == len(popped)


if __name__ == '__main__':
    solution = Solution()

    assert solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    assert not solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
