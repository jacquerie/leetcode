# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        frequencies = [self.getFrequencyOfSmallest(word) for word in words]
        frequency_counts = Counter(frequencies)

        result = []

        for query in queries:
            frequency = self.getFrequencyOfSmallest(query)
            bigger_frequency_counts = [
                el for el in frequency_counts.keys() if el > frequency]
            num_of_bigger_frequency_counts = sum(
                frequency_counts[el] for el in bigger_frequency_counts)
            result.append(num_of_bigger_frequency_counts)

        return result

    def getFrequencyOfSmallest(self, word):
        return word.count(min(word))


if __name__ == '__main__':
    solution = Solution()

    assert [1] == solution.numSmallerByFrequency(['cbd'], ['zaaaz'])
    assert [1, 2] == solution.numSmallerByFrequency(['bbb', 'cc'], ['a', 'aa', 'aaa', 'aaaa'])
