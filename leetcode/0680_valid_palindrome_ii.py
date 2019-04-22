# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def validPalindrome(self, s):
        def _validPalindrome(s, first, last):
            while first < last:
                if s[first] != s[last]:
                    return False
                first, last = first + 1, last - 1
            return True

        first, last = 0, len(s) - 1
        while first < last:
            if s[first] != s[last]:
                return _validPalindrome(s, first, last - 1) or _validPalindrome(s, first + 1, last)
            first, last = first + 1, last - 1
        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.validPalindrome('aba')
    assert solution.validPalindrome('abca')
