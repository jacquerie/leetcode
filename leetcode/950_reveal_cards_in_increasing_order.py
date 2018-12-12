# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import deque


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        queue = deque()
        for card in sorted(deck, reverse=True):
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)

        return list(queue)


if __name__ == '__main__':
    solution = Solution()

    assert [2, 13, 3, 11, 5, 17, 7] == solution.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
