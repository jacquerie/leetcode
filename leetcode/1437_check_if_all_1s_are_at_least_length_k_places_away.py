# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = None
        for index, num in enumerate(nums):
            if num == 1:
                if last_index is not None and index - last_index <= k:
                    return False
                else:
                    last_index = index
        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2)
    assert not solution.kLengthApart([1, 0, 0, 1, 0, 1], 2)
    assert solution.kLengthApart([1, 1, 1, 1, 1], 0)
    assert solution.kLengthApart([0, 1, 0, 1], 1)
