# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max, result = -1, []
        for el in reversed(arr):
            result.append(current_max)
            current_max = max(current_max, el)
        return list(reversed(result))


if __name__ == '__main__':
    solution = Solution()

    assert [18, 6, 6, 6, 1, -1] == solution.replaceElements([17, 18, 5, 4, 6, 1])
