# -*- coding: utf-8 -*-


class Solution(object):
    def hasAlternatingBits(self, n):
        b = bin(n)

        if '00' in b or '11' in b:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.hasAlternatingBits(5)
    assert not solution.hasAlternatingBits(7)
    assert solution.hasAlternatingBits(10)
    assert not solution.hasAlternatingBits(11)
