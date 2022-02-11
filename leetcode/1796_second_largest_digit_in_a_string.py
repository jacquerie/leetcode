# -*- coding: utf-8 -*-


class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(c) for c in s if c.isdigit()}
        if len(digits) < 2:
            return -1
        *_, result, _ = sorted(list(digits))
        return result


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.secondHighest("dfa12321afd")
    assert -1 == solution.secondHighest("abc1111")
    assert 0 == solution.secondHighest("ck077")
