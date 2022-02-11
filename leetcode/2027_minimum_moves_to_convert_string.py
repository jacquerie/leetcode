# -*- coding: utf-8 -*-


class Solution:
    def minimumMoves(self, s: str) -> int:
        chars, result = list(s), 0
        for i, char in enumerate(chars):
            if char == "X":
                chars[i : i + 3], result = ["O", "O", "O"], result + 1
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.minimumMoves("XXX")
    assert 2 == solution.minimumMoves("XXOX")
    assert 0 == solution.minimumMoves("000")
