# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def minAddToMakeValid(self, S):
        open_count, result = 0, 0

        for c in S:
            if c == ')' and open_count == 0:
                result += 1
            elif c == ')':
                open_count -= 1
            else:
                open_count += 1

        return open_count + result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minAddToMakeValid('())')
    assert 3 == solution.minAddToMakeValid('(((')
    assert 0 == solution.minAddToMakeValid('()')
    assert 4 == solution.minAddToMakeValid('()))((')
