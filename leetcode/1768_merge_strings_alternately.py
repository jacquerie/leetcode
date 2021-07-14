# -*- coding: utf-8 -*-

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result, i, j = [], 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'apbqcr' == solution.mergeAlternately('abc', 'pqr')
    assert 'apbqrs' == solution.mergeAlternately('ab', 'pqrs')
    assert 'apbqcd' == solution.mergeAlternately('abcd', 'pq')
