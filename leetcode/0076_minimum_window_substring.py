# -*- coding: utf-8 -*-

from collections import Counter, defaultdict, deque


class Solution(object):
    def minWindow(self, s, t):
        best_first, best_last, best_length = 0, len(s) - 1, len(s) + 1
        counts, occurrences = Counter(t), defaultdict(deque)

        for i, c in enumerate(s):
            if c not in counts:
                continue

            occurrences[c].append(i)
            if counts[c] < len(occurrences[c]):
                occurrences[c].popleft()

            if best_length == len(s) + 1:
                if any(counts[c] > len(occurrences[c]) for c in counts):
                    continue

            current_first = min(occurrences[c][0] for c in counts)
            current_last = max(occurrences[c][-1] for c in counts) + 1
            if current_last - current_first < best_length:
                best_first = current_first
                best_last = current_last
                best_length = current_last - current_first

        return s[best_first:best_last] if best_length != len(s) + 1 else ''


if __name__ == '__main__':
    solution = Solution()

    assert 'BANC' == solution.minWindow('ADOBECODEBANC', 'ABC')
    assert 'aa' == solution.minWindow('aa', 'aa')
    assert '' == solution.minWindow('a', 'b')
    assert 'cwae' == solution.minWindow('cabwefgewcwaefgcf', 'cae')
