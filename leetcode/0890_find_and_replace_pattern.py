# -*- coding: utf-8 -*-


class Solution:
    def findAndReplacePattern(self, words, pattern):
        result = []

        for word in words:
            if self.wordMatchesPattern(word, pattern):
                result.append(word)

        return result

    def wordMatchesPattern(self, word, pattern):
        if len(word) != len(pattern):
            return False

        seen_w, seen_p = {}, {}
        for w, p in zip(word, pattern):
            if w in seen_w and seen_w[w] != p:
                return False
            if p in seen_p and seen_p[p] != w:
                return False
            seen_w[w] = p
            seen_p[p] = w

        return True


if __name__ == "__main__":
    solution = Solution()

    assert ["mee", "aqq"] == solution.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"
    )
