# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os


class Solution(object):
    def simplifyPath(self, path):
        return os.path.realpath(path)


if __name__ == '__main__':
    solution = Solution()

    assert '/home' == solution.simplifyPath('/home')
    assert '/c' == solution.simplifyPath('/a/./b/../../c')
    assert '/' == solution.simplifyPath('/../')
    assert '/home/foo' == solution.simplifyPath('/home//foo')
