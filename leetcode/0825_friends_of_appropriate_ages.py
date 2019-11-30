# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def numFriendRequests(self, ages):
        result = 0

        counts = Counter(ages)
        for age1, count1 in counts.items():
            for age2, count2 in counts.items():
                if age1 // 2 + 7 < age2 <= age1:
                    result += count1 * (count2 - (1 if age1 == age2 else 0))

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.numFriendRequests([16, 16])
    assert 2 == solution.numFriendRequests([16, 17, 18])
    assert 3 == solution.numFriendRequests([20, 30, 100, 110, 120])
    assert 3 == solution.numFriendRequests([108, 115, 5, 24, 82])
