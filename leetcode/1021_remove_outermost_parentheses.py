# -*- coding: utf-8 -*-


class Solution:
    def removeOuterParentheses(self, S):
        result = []

        count = 0
        for c in S:
            if c == "(":
                if count > 0:
                    result.append(c)
                count += 1
            elif c == ")":
                if count > 1:
                    result.append(c)
                count -= 1

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert "()()()" == solution.removeOuterParentheses("(()())(())")
    assert "()()()()(())" == solution.removeOuterParentheses("(()())(())(()(()))")
    assert "" == solution.removeOuterParentheses("()()")
