# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):

    ROWS = [
        set(['Q', 'W', 'E', 'R', 'T', 'Y', 'I', 'U', 'O', 'P']),
        set(['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']),
        set(['Z', 'X', 'C', 'V', 'B', 'N', 'M']),
    ]

    def findWords(self, words):
        return [
            word for word in words if any(
                all(char in row for char in word.upper()) for row in self.ROWS)]


if __name__ == '__main__':
    solution = Solution()

    assert ['Alaska', 'Dad'] == solution.findWords(['Hello', 'Alaska', 'Dad', 'Peace'])
