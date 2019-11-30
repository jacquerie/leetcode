# -*- coding: utf-8 -*-


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)

        result = []

        i = 0
        while i < len(intervals):
            newInterval = Interval(intervals[i].start, intervals[i].end)
            i += 1
            while i < len(intervals) and intervals[i].start <= newInterval.end:
                newInterval = Interval(
                    min(newInterval.start, intervals[i].start),
                    max(newInterval.end, intervals[i].end))
                i += 1
            result.append(newInterval)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
        Interval(1, 6),
        Interval(8, 10),
        Interval(15, 18),
    ] == solution.merge([
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18),
    ])
    assert [
        Interval(1, 5),
    ] == solution.merge([
        Interval(1, 4),
        Interval(4, 5),
    ])
    assert [
        Interval(0, 0),
        Interval(1, 4),
    ] == solution.merge([
        Interval(1, 4),
        Interval(0, 0),
    ])
