# -*- coding: utf-8 -*-


class Solution:
    def numJewelsInStones(self, J, S):
        return len([c for c in S if c in set(J)])


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numJewelsInStones('aA', 'aAAbbbb')
    assert 0 == solution.numJewelsInStones('z', 'ZZ')
