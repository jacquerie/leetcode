# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences, result = [], 0
        for a_cost, b_cost in costs:
            differences.append(a_cost - b_cost)
            result += a_cost
        differences.sort(reverse=True)
        return result - sum(differences[: len(costs) // 2])


if __name__ == "__main__":
    solution = Solution()

    assert 110 == solution.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
