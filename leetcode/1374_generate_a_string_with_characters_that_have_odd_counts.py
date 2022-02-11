# -*- coding: utf-8 -*-


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a" * n
        return "a" * (n - 1) + "b"


if __name__ == "__main__":
    solution = Solution()

    assert "aaab" == solution.generateTheString(4)
    assert "ab" == solution.generateTheString(2)
    assert "aaaaaaa" == solution.generateTheString(7)
