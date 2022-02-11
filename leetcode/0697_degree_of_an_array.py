# -*- coding: utf-8 -*-

from collections import namedtuple

Occurrence = namedtuple("Occurrence", ["min", "max", "count"])


class Solution:
    def findShortestSubArray(self, nums):
        occurrences = {}
        for i, num in enumerate(nums):
            if num in occurrences:
                occurrence = occurrences[num]
                occurrences[num] = Occurrence(
                    min=occurrence.min, max=i, count=occurrence.count + 1
                )
            else:
                occurrences[num] = Occurrence(min=i, max=i, count=1)

        result = float("inf")

        max_count = max(occurrence.count for occurrence in occurrences.values())
        for occurrence in occurrences.values():
            if occurrence.count == max_count:
                result = min(result, occurrence.max - occurrence.min + 1)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.findShortestSubArray([1, 2, 2, 3, 1])
    assert 6 == solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
