# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
            else:
                result.append(prices[i])
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [4, 2, 4, 2, 3] == solution.finalPrices([8, 4, 6, 2, 3])
    assert [1, 2, 3, 4, 5] == solution.finalPrices([1, 2, 3, 4, 5])
    assert [9, 0, 1, 6] == solution.finalPrices([10, 1, 1, 6])
