# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_lasers, result = 0, 0
        for row in bank:
            current_lasers = row.count("1")
            if current_lasers and last_lasers:
                result += current_lasers * last_lasers
            if current_lasers:
                last_lasers = current_lasers
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 8 == solution.numberOfBeams(["011001", "000000", "010100", "001000"])
    assert 0 == solution.numberOfBeams(["000", "111", "000"])
