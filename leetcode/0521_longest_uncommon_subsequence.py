# -*- coding: utf-8 -*-


class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.findLUSlength("aba", "cdc")
