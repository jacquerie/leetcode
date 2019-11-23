# -*- coding: utf-8 -*-


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(
                min(newInterval.start, intervals[i].start),
                max(newInterval.end, intervals[i].end))
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
        Interval(1, 5),
        Interval(6, 9),
    ] == solution.insert([
        Interval(1, 3),
        Interval(6, 9),
    ], Interval(2, 5))
    assert [
        Interval(1, 2),
        Interval(3, 10),
        Interval(12, 16),
    ] == solution.insert([
        Interval(1, 2),
        Interval(3, 5),
        Interval(6, 7),
        Interval(8, 10),
        Interval(12, 16),
    ], Interval(4, 8))
