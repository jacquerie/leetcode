# -*- coding: utf-8 -*-

import itertools


class Solution:
    def numTilePossibilities(self, tiles):
        return sum(
            len(set(itertools.permutations(tiles, i))) for i in range(1, len(tiles) + 1)
        )


if __name__ == "__main__":
    solution = Solution()

    assert 8 == solution.numTilePossibilities("AAB")
    assert 188 == solution.numTilePossibilities("AAABBC")
