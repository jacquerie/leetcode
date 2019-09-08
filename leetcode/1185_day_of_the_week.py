# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import datetime


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        return datetime.date(year, month, day).strftime('%A')


if __name__ == '__main__':
    solution = Solution()

    assert 'Saturday' == solution.dayOfTheWeek(31, 8, 2019)
    assert 'Sunday' == solution.dayOfTheWeek(18, 7, 1999)
    assert 'Sunday' == solution.dayOfTheWeek(15, 8, 1993)
