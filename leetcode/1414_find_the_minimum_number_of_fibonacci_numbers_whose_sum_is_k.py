# -*- coding: utf-8 -*-

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 0:
            return 0
        elif k == 1:
            return 1
        elif k == 2:
            return 1

        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return 1 + self.findMinFibonacciNumbers(k - a)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.findMinFibonacciNumbers(7)
    assert 2 == solution.findMinFibonacciNumbers(10)
    assert 3 == solution.findMinFibonacciNumbers(19)
