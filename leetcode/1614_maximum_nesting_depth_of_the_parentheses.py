# -*- coding: utf-8 -*-


class Solution:
    def maxDepth(self, s: str) -> int:
        current, result = 0, 0
        for c in s:
            if c == '(':
                current += 1
            elif c == ')':
                current -= 1
            result = max(current, result)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.maxDepth('(1+(2*3)+((8)/4))+1')
    assert 3 == solution.maxDepth('(1)+((2))+(((3)))')
    assert 1 == solution.maxDepth('1+(2*3)/(2-1)')
    assert 0 == solution.maxDepth('1')
