# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countSetBits(self, n: int) -> int:
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda el: (self.countSetBits(el), el))


if __name__ == "__main__":
    solution = Solution()

    assert [0, 1, 2, 4, 8, 3, 5, 6, 7] == solution.sortByBits(
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
    )
    assert [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] == solution.sortByBits(
        [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    )
    assert [10000, 10000] == solution.sortByBits([10000, 10000])
    assert [2, 3, 5, 17, 7, 11, 13, 19] == solution.sortByBits(
        [2, 3, 5, 7, 11, 13, 17, 19]
    )
    assert [10, 100, 10000, 1000] == solution.sortByBits([10, 100, 1000, 10000])
