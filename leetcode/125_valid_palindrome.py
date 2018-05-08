# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import re


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]+', '', s)

        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPalindrome('A man, a plan, a canal: Panama')
    assert not solution.isPalindrome('race a car')
