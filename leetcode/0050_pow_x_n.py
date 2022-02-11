# -*- coding: utf-8 -*-


def almost_equal(x, y, rel_tol=1e-09, abs_tol=0.0):
    return abs(x - y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)


class Solution:
    def myPow(self, x, n):
        positive = True
        if n < 0:
            n, positive = -n, False

        result = 1.0
        while n:
            if n & 1:
                result *= x
            n >>= 1
            x *= x

        return result if positive else 1.0 / result


if __name__ == "__main__":
    solution = Solution()

    assert almost_equal(1024.0, solution.myPow(2.0, 10))
    assert almost_equal(9.261, solution.myPow(2.1, 3))
    assert almost_equal(0.25, solution.myPow(2.0, -2))
