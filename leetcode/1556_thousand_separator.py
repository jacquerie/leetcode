# -*- coding: utf-8 -*-

class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = []

        n_str = str(n)
        for i, char in enumerate(reversed(n_str), 1):
            result.append(char)
            if i % 3 == 0 and i < len(n_str):
                result.append('.')

        return ''.join(reversed(result))


if __name__ == '__main__':
    solution = Solution()

    assert '987' == solution.thousandSeparator(987)
    assert '1.234' == solution.thousandSeparator(1234)
    assert '123.456.789' == solution.thousandSeparator(123456789)
    assert '0' == solution.thousandSeparator(0)
