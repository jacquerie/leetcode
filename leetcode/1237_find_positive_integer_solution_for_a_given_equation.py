# -*- coding: utf-8 -*-


class CustomFunction:
    def __init__(self, f):
        self.f = f


class Solution:
    def findSolution(self, customfunction, z):
        result = []

        for x in range(1, 1001):
            for y in range(1, 1001):
                f = customfunction.f(x, y)
                if f > z:
                    break
                elif f == z:
                    result.append([x, y])

        return result


if __name__ == "__main__":
    solution = Solution()

    assert [[1, 4], [2, 3], [3, 2], [4, 1]] == solution.findSolution(
        CustomFunction(lambda x, y: x + y), 5
    )
    assert [[1, 5], [5, 1]] == solution.findSolution(
        CustomFunction(lambda x, y: x * y), 5
    )
