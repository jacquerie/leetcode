# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Solution(object):
    def countAndSay(self, n):
        result = '1'

        for _ in range(n - 1):
            partial = []
            for el, group in itertools.groupby(result):
                partial.append(str(len(list(group))))
                partial.append(el)
            result = ''.join(partial)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert '1' == solution.countAndSay(1)
    assert '1211' == solution.countAndSay(4)
