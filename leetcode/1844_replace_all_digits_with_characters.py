# -*- coding: utf-8 -*-

class Solution:
    def replaceDigits(self, s: str) -> str:
        result = list(s)
        for i in range(1, len(result), 2):
            result[i] = self.shift(result[i - 1], int(result[i]))
        return ''.join(result)

    def shift(self, c: str, x: int) -> str:
        return chr(ord(c) + x)


if __name__ == '__main__':
    solution = Solution()

    assert 'abcdef' == solution.replaceDigits('a1c1e1')
    assert 'abbdcfdhe' == solution.replaceDigits('a1b2c3d4e')
