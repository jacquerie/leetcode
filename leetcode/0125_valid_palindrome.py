# -*- coding: utf-8 -*-

import re


class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub("[^a-z0-9]+", "", s)

        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama")
    assert not solution.isPalindrome("race a car")
