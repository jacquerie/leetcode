# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def countPrimeSetBits(self, L, R):
        def countSetBits(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        result = 0

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for n in xrange(L, R + 1):
            if countSetBits(n) in primes:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.countPrimeSetBits(6, 10)
    assert 5 == solution.countPrimeSetBits(10, 15)
