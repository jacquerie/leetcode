# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        seen = set()

        for i in range(4):
            el = arr[(i * len(arr)) // 4]
            if el in seen:
                return el
            seen.add(el)

        for i in range(4):
            el = arr[((2 * i + 1) * len(arr)) // 8]
            if el in seen:
                return el


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])
