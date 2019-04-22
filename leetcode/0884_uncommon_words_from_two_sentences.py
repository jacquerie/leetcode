# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, A, B):
        counts = Counter(A.split())
        for word in B.split():
            counts[word] += 1

        result = []

        for word, count in counts.iteritems():
            if count == 1:
                result.append(word)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert ['sour', 'sweet'] == sorted(solution.uncommonFromSentences('this apple is sweet', 'this apple is sour'))
    assert ['banana'] == sorted(solution.uncommonFromSentences('apple apple', 'banana'))
