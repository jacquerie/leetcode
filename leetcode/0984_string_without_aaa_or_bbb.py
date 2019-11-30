# -*- coding: utf-8 -*-


class Solution:
    def strWithout3a3b(self, A, B):
        if A >= 2 * B:
            result = ['aab'] * B + ['a'] * (A - 2 * B)
        elif A >= B:
            result = ['aab'] * (A - B) + ['ab'] * (2 * B - A)
        elif B >= 2 * A:
            result = ['bba'] * A + ['b'] * (B - 2 * A)
        else:
            result = ['bba'] * (B - A) + ['ab'] * (2 * A - B)
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'bba' == solution.strWithout3a3b(1, 2)
    assert 'aabaa' == solution.strWithout3a3b(4, 1)
