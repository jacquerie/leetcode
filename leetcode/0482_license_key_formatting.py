# -*- coding: utf-8 -*-


class Solution:
    def licenseKeyFormatting(self, S, K):
        S = S.upper()
        S = ''.join(S.split('-'))
        S = S[::-1]

        parts = [S[i:i + K] for i in range(0, len(S), K)]
        return '-'.join(parts)[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert '5F3Z-2E9W' == solution.licenseKeyFormatting('5F3Z-2e-9-w', 4)
    assert '2-5G-3J' == solution.licenseKeyFormatting('2-5g-3-J', 2)
