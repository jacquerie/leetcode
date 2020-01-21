# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        prefix_sum, total_sum = 0, sum(A)

        for i, el in enumerate(A):
            prefix_sum += el
            if prefix_sum == total_sum // 3:
                current_sum = 0
                for j in range(i + 1, len(A)):
                    current_sum += A[j]
                    if current_sum == total_sum // 3:
                        return True

        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    assert not solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
    assert solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
