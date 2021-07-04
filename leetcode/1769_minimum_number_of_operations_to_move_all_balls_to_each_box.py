# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)

        left_count, left_total = 0, 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                left_count += 1
            left_total += left_count
            result[i] += left_total

        right_count, right_total = 0, 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                right_count += 1
            right_total += right_count
            result[i] += right_total

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [1, 1, 3] == solution.minOperations('110')
    assert [11, 8, 5, 4, 3, 4] == solution.minOperations('001011')
