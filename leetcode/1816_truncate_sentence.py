# -*- coding: utf-8 -*-


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


if __name__ == "__main__":
    solution = Solution()

    assert "Hello how are you" == solution.truncateSentence(
        "Hello how are you Contestant", 4
    )
    assert "What is the solution" == solution.truncateSentence(
        "What is the solution to this problem", 4
    )
    assert "chopper is not a tanuki" == solution.truncateSentence(
        "chopper is not a tanuki", 5
    )
