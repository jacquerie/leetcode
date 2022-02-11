# -*- coding: utf-8 -*-


class Solution:
    def longestWord(self, words):
        wordsSet = set(words)
        result = []

        for word in words:
            if all(word[:i] in wordsSet for i in range(1, len(word))):
                result.append(word)

        return min(result, key=lambda el: (-len(el), el))


if __name__ == "__main__":
    solution = Solution()

    assert "world" == solution.longestWord(["w", "wo", "wor", "worl", "world"])
    assert "apple" == solution.longestWord(
        ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    )
