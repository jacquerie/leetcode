# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


if __name__ == "__main__":
    solution = Solution()

    assert 2500.0 == solution.average([4000, 3000, 1000, 2000])
    assert 2000.0 == solution.average([1000, 2000, 3000])
    assert 3500.0 == solution.average([6000, 5000, 4000, 3000, 2000, 1000])
    assert 4750.0 == solution.average([8000, 9000, 2000, 3000, 6000, 1000])
