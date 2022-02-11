# -*- coding: utf-8 -*-


class Solution:
    def scoreOfParentheses(self, S):
        current_depth, result = 0, 0

        for i, c in enumerate(S):
            if c == "(":
                current_depth += 1
            else:
                current_depth -= 1
                if S[i - 1] == "(":
                    result += 2**current_depth

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.scoreOfParentheses("()")
    assert 2 == solution.scoreOfParentheses("(())")
    assert 2 == solution.scoreOfParentheses("()()")
    assert 6 == solution.scoreOfParentheses("(()(()))")
