# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def numJewelsInStones(self, J, S):
        return len([c for c in S if c in set(J)])


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numJewelsInStones('aA', 'aAAbbbb')
    assert 0 == solution.numJewelsInStones('z', 'ZZ')
