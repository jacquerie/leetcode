# -*- coding: utf-8 -*-

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        frontier = deque([start])
        while frontier:
            current = frontier.pop()
            if 0 <= current < len(arr) and arr[current] >= 0:
                arr[current] = -arr[current]
                if arr[current] == 0:
                    return True
                frontier.append(current + arr[current])
                frontier.append(current - arr[current])
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 5)
    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 0)
    assert not solution.canReach([3, 0, 2, 1, 2], 2)
