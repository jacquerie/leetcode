# -*- coding: utf-8 -*-


class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            x, y, z = 0, 1, 1
            for _ in range(3, n + 1):
                x, y, z = y, z, x + y + z
            return z


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.tribonacci(4)
    assert 1389537 == solution.tribonacci(25)
