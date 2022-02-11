# -*- coding: utf-8 -*-


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(c) for c in n)


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.minPartitions("32")
    assert 8 == solution.minPartitions("82374")
    assert 9 == solution.minPartitions("27346209830709182346")
