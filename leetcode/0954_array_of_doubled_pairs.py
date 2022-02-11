# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def canReorderDoubled(self, A):
        counts = Counter(A)
        for el in sorted(counts, key=abs):
            if counts[2 * el] < counts[el]:
                return False
            counts[2 * el] -= counts[el]
        return True


if __name__ == "__main__":
    solution = Solution()

    assert not solution.canReorderDoubled([3, 1, 3, 6])
    assert not solution.canReorderDoubled([2, 1, 2, 6])
    assert solution.canReorderDoubled([4, -2, 2, -4])
    assert not solution.canReorderDoubled([1, 2, 4, 16, 8, 4])
