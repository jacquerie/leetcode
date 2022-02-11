# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return 1 + max(sentence.count(" ") for sentence in sentences)


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.mostWordsFound(
        [
            "alice and bob love leetcode",
            "i think so too",
            "this is great thanks very much",
        ]
    )
    assert 3 == solution.mostWordsFound(
        ["please wait", "continue to fight", "continue to win"]
    )
