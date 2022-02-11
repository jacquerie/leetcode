# -*- coding: utf-8 -*-


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        result = [0] * (amount + 1)

        for i in range(amount + 1):
            partial = float("inf")
            for coin in coins:
                if i - coin == 0:
                    partial = 1
                elif i - coin > 0:
                    partial = min(partial, 1 + result[i - coin])
            result[i] = partial

        return -1 if result[-1] == float("inf") else result[-1]


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.coinChange([1, 2, 5], 11)
    assert -1 == solution.coinChange([2], 3)
