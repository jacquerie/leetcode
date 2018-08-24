# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        current_first, result = 0, 0

        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                if seen[c] >= current_first:
                    result = max(result, i - current_first)
                    current_first = seen[c] + 1
            seen[c] = i

        return max(result, len(s) - current_first)


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.lengthOfLongestSubstring('abcabcbb')
    assert 1 == solution.lengthOfLongestSubstring('bbbbb')
    assert 3 == solution.lengthOfLongestSubstring('pwwkew')
    assert 2 == solution.lengthOfLongestSubstring('aab')
