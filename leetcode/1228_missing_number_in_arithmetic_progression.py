# -*- coding: utf-8 -*-


class Solution:
    def missingNumber(self, arr):
        return ((arr[-1] + arr[0]) * (len(arr) + 1)) // 2 - sum(arr)


if __name__ == '__main__':
    solution = Solution()

    assert 9 == solution.missingNumber([5, 7, 11, 13])
    assert 14 == solution.missingNumber([15, 13, 12])
    assert 0 == solution.missingNumber([0, 0, 0, 0, 0])
