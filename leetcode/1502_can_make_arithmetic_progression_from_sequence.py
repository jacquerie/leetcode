# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        return all(el == arr[0] + i * diff for i, el in enumerate(arr))


if __name__ == '__main__':
    solution = Solution()

    assert solution.canMakeArithmeticProgression([3, 5, 1])
    assert not solution.canMakeArithmeticProgression([1, 2, 4])
