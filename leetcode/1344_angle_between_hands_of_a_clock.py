# -*- coding: utf-8 -*-


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = 6 * minutes
        hour_angle = (30 * hour + minutes / 2) % 360
        angle = abs(minutes_angle - hour_angle)
        return angle if angle <= 180 else 360 - angle


if __name__ == '__main__':
    solution = Solution()

    assert 165 == solution.angleClock(12, 30)
    assert 75 == solution.angleClock(3, 30)
    assert 7.5 == solution.angleClock(3, 15)
    assert 155 == solution.angleClock(4, 50)
    assert 0 == solution.angleClock(12, 0)
    assert 76.5 == solution.angleClock(1, 57)
