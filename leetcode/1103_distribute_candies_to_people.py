# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i, current, result = 0, 1, [0] * num_people
        while candies:
            candies -= current
            result[i] += current
            i, current = (i + 1) % num_people, min(current + 1, candies)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [1, 2, 3, 1] == solution.distributeCandies(7, 4)
    assert [5, 2, 3] == solution.distributeCandies(10, 3)
