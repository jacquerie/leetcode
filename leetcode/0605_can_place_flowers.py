# -*- coding: utf-8 -*-


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            previous = i == 0 or flowerbed[i - 1] == 0
            current = flowerbed[i] == 0
            next = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            if previous and current and next:
                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert not solution.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    assert not solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
    assert solution.canPlaceFlowers([0, 0, 0, 0, 0, 1, 0, 0], 0)
