# -*- coding: utf-8 -*-

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            result = sum(int(digit) for digit in str(result))
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 36 == solution.getLucky('iiii', 1)
    assert 6 == solution.getLucky('leetcode', 2)
