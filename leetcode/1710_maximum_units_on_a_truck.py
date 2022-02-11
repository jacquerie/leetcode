# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box_types, result = (
            sorted(boxTypes, key=lambda el: el[1], reverse=True),
            0,
        )
        for number_of_boxes, number_of_units_per_box in sorted_box_types:
            number_of_boxes_taken = min(number_of_boxes, truckSize)
            result += number_of_boxes_taken * number_of_units_per_box
            truckSize -= number_of_boxes_taken
            if not truckSize:
                break
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 8 == solution.maximumUnits([[1, 3], [2, 2], [3, 1]], 4)
    assert 91 == solution.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10)
