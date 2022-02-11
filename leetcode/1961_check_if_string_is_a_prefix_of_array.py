# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        current_prefix = ""
        for word in words:
            current_prefix += word
            if current_prefix == s:
                return True
            elif len(current_prefix) > len(s):
                return False
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"])
    assert not solution.isPrefixString(
        "iloveleetcode", ["apples", "i", "love", "leetcode"]
    )
    assert not solution.isPrefixString("a", ["aa", "aaaa", "banana"])
