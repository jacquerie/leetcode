# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        result = duration * len(timeSeries)
        for i in xrange(1, len(timeSeries)):
            result -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.findPoisonedDuration([1, 4], 2)
    assert 3 == solution.findPoisonedDuration([1, 2], 2)
