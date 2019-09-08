# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if destination < start:
            start, destination = destination, start

        return min(
            sum(distance[start:destination]),
            sum(distance[:start]) + sum(distance[destination:])
        )


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 1)
    assert 3 == solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 2)
    assert 4 == solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 3)
