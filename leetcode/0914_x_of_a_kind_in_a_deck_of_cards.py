# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()

        min_count = min(counts)
        if min_count == 1:
            return False

        partition_size = min_count
        for count in counts:
            remainder = count % min_count
            if remainder > 1:
                partition_size = min(partition_size, remainder)

        return all(count % partition_size == 0 for count in counts)


if __name__ == "__main__":
    solution = Solution()

    assert solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
    assert not solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])
    assert not solution.hasGroupsSizeX([1])
    assert solution.hasGroupsSizeX([1, 1])
    assert solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2])
    assert solution.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2])
