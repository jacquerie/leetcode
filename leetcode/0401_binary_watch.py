# -*- coding: utf-8 -*-

import itertools


class Solution:
    def readBinaryWatch(self, num):
        result = []
        for combination in itertools.combinations(range(10), num):
            time = self.binaryToTime(self.combinationToBinary(combination))
            if time is not None:
                result.append(time)
        return result

    def combinationToBinary(self, combination):
        result = ["0"] * 10
        for i in combination:
            result[i] = "1"
        return result

    def binaryToTime(self, binary):
        hour = int("".join(binary[:4]), 2)
        minutes = int("".join(binary[4:]), 2)
        if 0 <= hour < 12 and 0 <= minutes < 60:
            return "%d:%02d" % (hour, minutes)


if __name__ == "__main__":
    solution = Solution()

    assert [
        "8:00",
        "4:00",
        "2:00",
        "1:00",
        "0:32",
        "0:16",
        "0:08",
        "0:04",
        "0:02",
        "0:01",
    ] == solution.readBinaryWatch(1)
