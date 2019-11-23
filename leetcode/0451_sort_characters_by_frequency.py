# -*- coding: utf-8 -*-

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

    assert 'eetr' == solution.frequencySort('tree')
    assert 'cccaaa' == solution.frequencySort('cccaaa')
    assert 'bbAa' == solution.frequencySort('Aabb')
