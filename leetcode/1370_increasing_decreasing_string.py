# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        result = []

        counts = sorted([c, count] for c, count in Counter(s).items())
        while len(result) < len(s):
            for i, (c, count) in enumerate(counts):
                if count > 0:
                    result.append(c)
                    counts[i][1] -= 1
            for i, (c, count) in enumerate(reversed(counts)):
                if count > 0:
                    result.append(c)
                    counts[~i][1] -= 1

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert "abccbaabccba" == solution.sortString("aaaabbbbcccc")
    assert "art" == solution.sortString("rat")
    assert "cdelotee" == solution.sortString("leetcode")
    assert "ggggggg" == solution.sortString("ggggggg")
