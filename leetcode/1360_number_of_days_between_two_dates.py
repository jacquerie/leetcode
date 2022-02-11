# -*- coding: utf-8 -*-

from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(
            (
                datetime.strptime(date1, "%Y-%m-%d")
                - datetime.strptime(date2, "%Y-%m-%d")
            ).days
        )


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.daysBetweenDates("2019-06-29", "2019-06-30")
    assert 15 == solution.daysBetweenDates("2020-01-15", "2019-12-31")
