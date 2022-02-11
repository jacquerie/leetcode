# -*- coding: utf-8 -*-

from collections import deque


class Solution:
    def removeDuplicates(self, S):
        result = deque()

        for char in S:
            if result and char == result[-1]:
                result.pop()
            else:
                result.append(char)

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert "ca" == solution.removeDuplicates("abbaca")
