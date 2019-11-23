# -*- coding: utf-8 -*-

from collections import deque


class Solution(object):
    def shortestSubarray(self, A, K):
        prefix_sums = [0] * (len(A) + 1)
        for i, el in enumerate(A):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]

        result = float('inf')
        seen = deque()

        for i, prefix_sum in enumerate(prefix_sums):
            while seen and prefix_sum <= prefix_sums[seen[-1]]:
                seen.pop()
            while seen and prefix_sum - prefix_sums[seen[0]] >= K:
                result = min(result, i - seen.popleft())
            seen.append(i)

        return result if result != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.shortestSubarray([1], 1)
    assert -1 == solution.shortestSubarray([1, 2], 4)
    assert 3 == solution.shortestSubarray([2, -1, 2], 3)
