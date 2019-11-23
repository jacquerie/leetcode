# -*- coding: utf-8 -*-


class Solution(object):
    def crackSafe(self, n, k):
        if k == 1:
            return '0' * n
        s = self.deBrujin(n, k)
        return s + s[:n - 1]

    def deBrujin(self, n, k):
        """See: https://en.wikipedia.org/wiki/De_Bruijn_sequence#Algorithm"""
        def _deBrujin(t, p):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p + 1])
            else:
                a[t] = a[t - p]
                _deBrujin(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    _deBrujin(t + 1, t)

        a = [0] * k * n
        sequence = []
        _deBrujin(1, 1)
        return ''.join(str(el) for el in sequence)


if __name__ == '__main__':
    solution = Solution()

    assert '01' == solution.crackSafe(1, 2)
    assert '00110' == solution.crackSafe(2, 2)
    assert '0' == solution.crackSafe(1, 1)
    assert '00' == solution.crackSafe(2, 1)
