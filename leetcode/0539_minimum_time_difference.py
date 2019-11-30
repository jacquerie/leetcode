# -*- coding: utf-8 -*-


class Solution:
    def findMinDifference(self, timePoints):
        result = float('inf')

        times = sorted(self.toTimes(timePoints))
        for i in range(len(times)):
            if i == len(times) - 1:
                result = min(result, 1440 + times[0] - times[i])
            else:
                result = min(result, times[i + 1] - times[i])

        return result

    def toTimes(self, timePoints):
        result = []
        for timePoint in timePoints:
            hour, minute = map(int, timePoint.split(':'))
            result.append(60 * hour + minute)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.findMinDifference(['23:59', '00:00'])
    assert 0 == solution.findMinDifference(['00:00', '23:59', '00:00'])
    assert 60 == solution.findMinDifference(['01:01', '02:01'])
