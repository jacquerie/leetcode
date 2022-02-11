# -*- coding: utf-8 -*-

import os


class Solution:
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


if __name__ == "__main__":
    solution = Solution()

    assert "fl" == solution.longestCommonPrefix(["flower", "flow", "flight"])
    assert "" == solution.longestCommonPrefix(["dog", "racecar", "car"])
