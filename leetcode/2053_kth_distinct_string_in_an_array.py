# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen, seen_twice = set(), set()
        for el in arr:
            if el in seen:
                seen_twice.add(el)
            seen.add(el)

        for el in arr:
            if el not in seen_twice and k > 1:
                k -= 1
            elif el not in seen_twice:
                return el
        return ""


if __name__ == "__main__":
    solution = Solution()

    assert "a" == solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2)
    assert "aaa" == solution.kthDistinct(["aaa", "aa", "a"], 1)
    assert "" == solution.kthDistinct(["a", "b", "a"], 3)
