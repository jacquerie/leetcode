# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation, result = list(range(1, m + 1)), []
        for query in queries:
            index = permutation.index(query)
            del permutation[index]
            permutation.insert(0, query)
            result.append(index)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [2, 1, 2, 1] == solution.processQueries([3, 1, 2, 1], 5)
    assert [3, 1, 2, 0] == solution.processQueries([4, 1, 2, 2], 4)
    assert [6, 5, 0, 7, 5] == solution.processQueries([7, 5, 5, 8, 3], 8)
