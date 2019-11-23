# -*- coding: utf-8 -*-

import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, words, k):
        counter = Counter(words)

        most_common = []
        for el in counter.items():
            heapq.heappush(most_common, (-el[1], el[0]))

        return [el[1] for el in heapq.nsmallest(k, most_common)]


if __name__ == '__main__':
    solution = Solution()

    assert ['i', 'love'] == solution.topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2)
    assert ['the', 'is', 'sunny', 'day'] == solution.topKFrequent(['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], 4)
    assert ['a'] == solution.topKFrequent(['aaa', 'aa', 'a'], 1)
