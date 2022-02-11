# -*- coding: utf-8 -*-


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.numberOfMatches(7)
    assert 13 == solution.numberOfMatches(14)
