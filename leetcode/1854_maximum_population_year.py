# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = []
        for birth, death in logs:
            changes.append((birth, 1))
            changes.append((death, -1))
        changes.sort()

        current_population, max_population, year_with_max_population = 0, 0, None
        for year, change in changes:
            current_population += change
            if current_population > max_population:
                max_population = current_population
                year_with_max_population = year
        return year_with_max_population


if __name__ == "__main__":
    solution = Solution()

    assert 1993 == solution.maximumPopulation([[1993, 1999], [2000, 2010]])
    assert 1960 == solution.maximumPopulation(
        [[1950, 1961], [1960, 1971], [1970, 1981]]
    )
