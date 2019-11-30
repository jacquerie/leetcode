# -*- coding: utf-8 -*-


def isBadVersion(n):
    return n >= 3


class Solution:
    def firstBadVersion(self, n):
        first, last = 1, n

        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1

        return first


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.firstBadVersion(5)
