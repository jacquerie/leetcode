# -*- coding: utf-8 -*-


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.wordToValue(firstWord) + self.wordToValue(
            secondWord
        ) == self.wordToValue(targetWord)

    def wordToValue(self, word: str) -> int:
        return int("".join(self.charToValue(char) for char in word))

    def charToValue(self, char: str) -> str:
        return str(ord(char) - ord("a"))


if __name__ == "__main__":
    solution = Solution()

    assert solution.isSumEqual("acb", "cba", "cdb")
    assert not solution.isSumEqual("aaa", "a", "aab")
    assert solution.isSumEqual("aaa", "a", "aaaa")
