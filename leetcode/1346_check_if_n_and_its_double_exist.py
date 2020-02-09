# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for el in arr:
            if el % 2 == 0 and el / 2 in seen:
                return True
            if 2 * el in seen:
                return True
            seen.add(el)

        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkIfExist([10, 2, 5, 3])
    assert solution.checkIfExist([7, 1, 14, 11])
    assert not solution.checkIfExist([3, 1, 7, 11])
