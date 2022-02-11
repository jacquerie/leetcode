# -*- coding: utf-8 -*-

import itertools


class Solution:
    def countBinarySubstrings(self, s):
        result = 0

        groups = [list(group) for _, group in itertools.groupby(s)]
        for i in range(len(groups) - 1):
            result += min(len(groups[i]), len(groups[i + 1]))

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.countBinarySubstrings("00110011")
    assert 4 == solution.countBinarySubstrings("10101")
