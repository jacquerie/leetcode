# -*- coding: utf-8 -*-


class Solution:
    def maxCoins(self, nums):
        def _maxCoins(i, j):
            if i == j:
                return 0

            if cache[i * n + j] == -1:
                prod = 1
                if i > 0:
                    prod *= nums[i - 1]
                if j < len(nums):
                    prod *= nums[j]

                cache[i * n + j] = max(
                    _maxCoins(i, k) + prod * nums[k] + _maxCoins(k + 1, j)
                    for k in range(i, j)
                )

            return cache[i * n + j]

        n = len(nums) + 1
        cache = [-1 for i in range(n) for j in range(n)]
        return _maxCoins(0, len(nums))


if __name__ == "__main__":
    solution = Solution()

    assert 167 == solution.maxCoins([3, 1, 5, 8])
