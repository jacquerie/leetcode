# -*- coding: utf-8 -*-


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return "".join(reversed(word[: word.find(ch) + 1])) + word[word.find(ch) + 1 :]


if __name__ == "__main__":
    solution = Solution()

    assert "dcbaefd" == solution.reversePrefix("abcdefd", "d")
    assert "zxyxxe" == solution.reversePrefix("xyxzxe", "z")
    assert "abcd" == solution.reversePrefix("abcd", "z")
