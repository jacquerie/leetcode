# -*- coding: utf-8 -*-


class Solution:
    def wordBreak(self, s, wordDict):
        if not s:
            return True

        wordSet = set(wordDict)
        result = [False] * (len(s) + 1)

        for i in range(len(s) + 1):
            if not result[i] and s[:i + 1] in wordSet:
                result[i] = True
            if result[i]:
                for j in range(i + 1, len(s) + 1):
                    if not result[j] and s[i + 1:j + 1] in wordSet:
                        result[j] = True

        return result[-1]


if __name__ == '__main__':
    solution = Solution()

    assert solution.wordBreak('leetcode', ['leet', 'code'])
    assert solution.wordBreak('applepenapple', ['apple', 'pen'])
    assert not solution.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
    assert not solution.wordBreak(150 * 'a' + 'b', ['a', 'aa'])
