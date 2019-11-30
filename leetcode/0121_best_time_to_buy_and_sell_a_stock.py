# -*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        minimum_price = float('inf')
        maximum_profit = 0

        for price in prices:
            if price < minimum_price:
                minimum_price = price
            if price - minimum_price > maximum_profit:
                maximum_profit = price - minimum_price

        return maximum_profit


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == solution.maxProfit([7, 6, 4, 3, 1])
