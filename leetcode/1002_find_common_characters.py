# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def commonChars(self, A):
        result = Counter(A[0])
        for el in A:
            result &= Counter(el)
        return list(result.elements())


if __name__ == '__main__':
    solution = Solution()

    assert ['e', 'l', 'l'] == solution.commonChars(['bella', 'label', 'roller'])
    assert ['c', 'o'] == solution.commonChars(['cool', 'lock', 'cook'])
