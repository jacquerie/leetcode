# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        counter = Counter(s)

        result = []
        for letter, count in counter.most_common():
            result.extend([letter] * count)

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'eert' == solution.frequencySort('tree')
    assert 'aaaccc' == solution.frequencySort('cccaaa')
    assert 'bbAa' == solution.frequencySort('Aabb')
