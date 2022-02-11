# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_square_side_length, result = float("-inf"), 0
        for length, width in rectangles:
            square_side_length = min(length, width)
            if square_side_length > max_square_side_length:
                max_square_side_length, result = square_side_length, 1
            elif square_side_length == max_square_side_length:
                result += 1
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]])
    assert 3 == solution.countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]])
