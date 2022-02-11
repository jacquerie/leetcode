# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        current_best, current_time, result = (
            releaseTimes[0],
            releaseTimes[0],
            keysPressed[0],
        )
        for time, key in zip(releaseTimes[1:], keysPressed[1:]):
            if (
                time - current_time > current_best
                or time - current_time == current_best
                and key > result
            ):
                current_best, result = time - current_time, key
            current_time = time
        return result


if __name__ == "__main__":
    solution = Solution()

    assert "c" == solution.slowestKey([9, 29, 49, 50], "cbcd")
    assert "a" == solution.slowestKey([12, 23, 36, 46, 62], "spuda")
