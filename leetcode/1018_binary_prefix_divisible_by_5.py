# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        current_prefix_value, result = 0, []
        for num in nums:
            current_prefix_value = 2 * current_prefix_value + num
            result.append(current_prefix_value % 5 == 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [True, False, False] == solution.prefixesDivBy5([0, 1, 1])
    assert [False, False, False] == solution.prefixesDivBy5([1, 1, 1])
    assert [True, False, False, False, True, False] == solution.prefixesDivBy5(
        [0, 1, 1, 1, 1, 1]
    )
    assert [False, False, False, False, False] == solution.prefixesDivBy5(
        [1, 1, 1, 0, 1]
    )
