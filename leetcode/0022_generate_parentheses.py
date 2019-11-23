# -*- coding: utf-8 -*-


class Solution(object):
    def generateParenthesis(self, n):
        result = []
        self._generateParenthesis(n, 0, 0, '', result)
        return result

    def _generateParenthesis(self, n, i, p, current, result):
        if i == 2 * n:
            if p == 0:
                result.append(current)
            return
        elif p < 0 or p > n:
            return

        self._generateParenthesis(n, i + 1, p + 1, current + '(', result)
        self._generateParenthesis(n, i + 1, p - 1, current + ')', result)


if __name__ == '__main__':
    solution = Solution()

    assert [
        '((()))',
        '(()())',
        '(())()',
        '()(())',
        '()()()',
    ] == solution.generateParenthesis(3)
