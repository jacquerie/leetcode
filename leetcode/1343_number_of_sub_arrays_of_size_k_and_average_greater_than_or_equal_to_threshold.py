# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum, i, result = 0, 0, 0

        while i < k - 1:
            current_sum += arr[i]
            i += 1

        while i < len(arr):
            current_sum += arr[i]
            if current_sum >= k * threshold:
                result += 1
            current_sum -= arr[i - k + 1]
            i += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    assert 5 == solution.numOfSubarrays([1, 1, 1, 1, 1], 1, 0)
    assert 6 == solution.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
    assert 1 == solution.numOfSubarrays([7, 7, 7, 7, 7, 7, 7], 7, 7)
    assert 1 == solution.numOfSubarrays([4, 4, 4, 4], 4, 1)
