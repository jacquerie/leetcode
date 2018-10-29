# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def wordSubsets(self, A, B):
        result = []

        b_universal_counter = Counter()
        for b in B:
            b_counter = Counter(b)
            self.toUniversal(b_counter, b_universal_counter)

        for a in A:
            a_counter = Counter(a)
            if self.isUniversal(a_counter, b_universal_counter):
                result.append(a)

        return result

    def toUniversal(self, b_counter, b_universal_counter):
        for char, count in b_counter.iteritems():
            b_universal_counter[char] = max(b_universal_counter[char], count)

    def isUniversal(self, a_counter, b_universal_counter):
        for char, count in b_universal_counter.iteritems():
            if char not in a_counter or a_counter[char] < count:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    assert ['facebook', 'google', 'leetcode'] == solution.wordSubsets([
        'amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'o'])
    assert ['apple', 'google', 'leetcode'] == solution.wordSubsets([
        'amazon', 'apple', 'facebook', 'google', 'leetcode'], ['l', 'e'])
    assert ['facebook', 'google'] == solution.wordSubsets([
        'amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'oo'])
    assert ['google', 'leetcode'] == solution.wordSubsets([
        'amazon', 'apple', 'facebook', 'google', 'leetcode'], ['lo', 'eo'])
    assert ['facebook', 'leetcode'] == solution.wordSubsets([
        'amazon', 'apple', 'facebook', 'google', 'leetcode'], ['ec', 'oc', 'ceo'])
