# -*- coding: utf-8 -*-


class Solution:
    def isOneBitCharacter(self, bits):
        return self._isOneBitCharacter(bits, 0, len(bits))

    def _isOneBitCharacter(self, bits, i, l):
        if i == l:
            return False
        elif i == l - 1:
            return True
        elif bits[i] == 1:
            return self._isOneBitCharacter(bits, i + 2, l)
        return self._isOneBitCharacter(bits, i + 1, l)


if __name__ == "__main__":
    solution = Solution()

    assert solution.isOneBitCharacter([1, 0, 0])
    assert not solution.isOneBitCharacter([1, 1, 1, 0])
    assert not solution.isOneBitCharacter([])
