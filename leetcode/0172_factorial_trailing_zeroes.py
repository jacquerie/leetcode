# -*- coding: utf-8 -*-


class Solution(object):
    def trailingZeroes(self, n):
        result = 0

        while n > 0:
            n //= 5
            result += n

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.trailingZeroes(3)
    assert 1 == solution.trailingZeroes(5)
    assert 24 == solution.trailingZeroes(100)
    assert 452137076 == solution.trailingZeroes(1808548329)
