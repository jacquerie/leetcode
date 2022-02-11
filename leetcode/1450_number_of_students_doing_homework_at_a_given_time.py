# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.busyStudent([1, 2, 3], [3, 2, 7], 4)
    assert 1 == solution.busyStudent([4], [4], 4)
    assert 0 == solution.busyStudent([4], [4], 5)
    assert 0 == solution.busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7)
    assert 5 == solution.busyStudent(
        [9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5
    )
