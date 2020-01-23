# -*- coding: utf-8 -*-

from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        return int(datetime.strptime(date, '%Y-%m-%d').strftime('%j'))


if __name__ == '__main__':
    solution = Solution()

    assert 9 == solution.dayOfYear('2019-01-09')
    assert 41 == solution.dayOfYear('2019-02-10')
    assert 60 == solution.dayOfYear('2003-03-01')
    assert 61 == solution.dayOfYear('2004-03-01')
