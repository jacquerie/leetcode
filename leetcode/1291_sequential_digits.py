# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [
            el
            for el in [
                12,
                23,
                34,
                45,
                56,
                67,
                78,
                89,
                123,
                234,
                345,
                456,
                567,
                678,
                789,
                1234,
                2345,
                3456,
                4567,
                5678,
                6789,
                12345,
                23456,
                34567,
                45678,
                56789,
                123456,
                234567,
                345678,
                456789,
                1234567,
                2345678,
                3456789,
                12345678,
                23456789,
                123456789,
            ]
            if low <= el <= high
        ]


if __name__ == "__main__":
    solution = Solution()

    assert [123, 234] == solution.sequentialDigits(100, 300)
    assert [1234, 2345, 3456, 4567, 5678, 6789, 12345] == solution.sequentialDigits(
        1000, 13000
    )
