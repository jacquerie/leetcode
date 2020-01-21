# -*- coding: utf-8 -*-


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join('1' if c == '0' else '0' for c in format(N, 'b')), 2)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.bitwiseComplement(5)
    assert 0 == solution.bitwiseComplement(7)
    assert 5 == solution.bitwiseComplement(10)
