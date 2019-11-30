# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)

        stack = deque()
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [1, 1, 4, 2, 1, 1, 0, 0] == solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
