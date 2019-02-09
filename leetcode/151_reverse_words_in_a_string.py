# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    solution = Solution()

    assert 'blue is sky the' == solution.reverseWords('the sky is blue')
