# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        for el in range(1, target[-1] + 1):
            result.append("Push")
            if el not in target:
                result.append("Pop")
        return result


if __name__ == "__main__":
    solution = Solution()

    assert ["Push", "Push", "Pop", "Push"] == solution.buildArray([1, 3], 3)
    assert ["Push", "Push", "Push"] == solution.buildArray([1, 2, 3], 3)
    assert ["Push", "Push"] == solution.buildArray([1, 2], 4)
    assert ["Push", "Pop", "Push", "Push", "Push"] == solution.buildArray([2, 3, 4], 4)
