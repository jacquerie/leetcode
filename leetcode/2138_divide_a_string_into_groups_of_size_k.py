# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k:
            s += fill * (k - len(s) % k)
        return [s[i : i + k] for i in range(0, len(s), k)]


if __name__ == "__main__":
    solution = Solution()

    assert ["abc", "def", "ghi"] == solution.divideString("abcdefghi", 3, "x")
    assert ["abc", "def", "ghi", "jxx"] == solution.divideString("abcdefghij", 3, "x")
