# -*- coding: utf-8 -*-

import random

random.seed(0)


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        x, y = 0, 0

        while not x or not y:
            roll = rand7()
            if 1 <= roll <= 2:
                x = roll
            elif 3 <= roll <= 7:
                y = roll

        return 5 * (x - 1) + (y - 2)


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.rand10()
