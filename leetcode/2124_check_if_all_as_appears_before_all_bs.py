# -*- coding: utf-8 -*-


class Solution:
    def checkString(self, s: str) -> bool:
        b_seen = False
        for char in s:
            if char == "a" and b_seen:
                return False
            if char == "b":
                b_seen = True
        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkString("aaabbb")
    assert not solution.checkString("abab")
    assert solution.checkString("bbb")
