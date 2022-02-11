# -*- coding: utf-8 -*-

import os


class Solution:
    def simplifyPath(self, path):
        return os.path.realpath(path)


if __name__ == "__main__":
    solution = Solution()

    assert "/home" == solution.simplifyPath("/home")
    assert "/c" == solution.simplifyPath("/a/./b/../../c")
    assert "/" == solution.simplifyPath("/../")
    assert "/home/foo" == solution.simplifyPath("/home//foo")
