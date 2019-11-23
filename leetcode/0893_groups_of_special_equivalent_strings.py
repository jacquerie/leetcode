# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def numSpecialEquivGroups(self, A):
        groups = set()
        for el in A:
            groups.add(self.toGroupNormalForm(el))
        return len(groups)

    def toGroupNormalForm(self, s):
        even, odd = Counter(), Counter()
        for i, c in enumerate(s):
            if i % 2 == 0:
                even[c] += 1
            else:
                odd[c] += 1
        return (
            self.toCounterNormalForm(even),
            self.toCounterNormalForm(odd),
        )

    def toCounterNormalForm(self, c):
        return tuple(sorted(c.items()))


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.numSpecialEquivGroups(['a', 'b', 'c', 'a', 'c', 'c'])
    assert 4 == solution.numSpecialEquivGroups(['aa', 'bb', 'ab', 'ba'])
    assert 3 == solution.numSpecialEquivGroups(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert 1 == solution.numSpecialEquivGroups(['abcd', 'cdab', 'adcb', 'cbad'])
