# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os


class Solution(object):
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


if __name__ == '__main__':
    solution = Solution()

    assert 'fl' == solution.longestCommonPrefix(['flower', 'flow', 'flight'])
    assert '' == solution.longestCommonPrefix(['dog', 'racecar', 'car'])
