# -*- coding: utf-8 -*-

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0


if __name__ == '__main__':
    solution = Solution()

    assert solution.isSameAfterReversals(526)
    assert not solution.isSameAfterReversals(1800)
    assert solution.isSameAfterReversals(0)
