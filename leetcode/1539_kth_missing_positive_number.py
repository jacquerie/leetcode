# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current_index, current_result = 0, 1
        while current_index < len(arr) and k > 0:
            if arr[current_index] == current_result:
                current_index += 1
            else:
                k -= 1
            current_result += 1
        return current_result + k - 1


if __name__ == "__main__":
    solution = Solution()

    assert 9 == solution.findKthPositive([2, 3, 4, 7, 11], 5)
    assert 6 == solution.findKthPositive([1, 2, 3, 4], 2)
