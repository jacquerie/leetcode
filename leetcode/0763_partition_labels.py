# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def partitionLabels(self, S):
        last_occurrences = {c: i for i, c in enumerate(S)}

        result = []
        current_first, current_last = 0, 0

        for i, c in enumerate(S):
            current_last = max(current_last, last_occurrences[c])
            if i == current_last:
                result.append(i - current_first + 1)
                current_first = i + 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert [9, 7, 8] == solution.partitionLabels('ababcbacadefegdehijhklij')
