# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        counts = defaultdict(list)
        for _id, size in enumerate(groupSizes):
            counts[size].append(_id)

        result = []
        for size, ids in sorted(counts.items()):
            for i in range(0, len(ids), size):
                result.append(ids[i:i + size])
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [[5], [0, 1, 2], [3, 4, 6]] == solution.groupThePeople([3, 3, 3, 3, 3, 1, 3])
    assert [[1], [0, 5], [2, 3, 4]] == solution.groupThePeople([2, 1, 3, 3, 3, 2])
