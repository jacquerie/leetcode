# -*- coding: utf-8 -*-


class Solution(object):
    def fib(self, N):
        current, next = 0, 1
        for _ in range(N):
            current, next = next, current + next
        return current


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.fib(2)
    assert 2 == solution.fib(3)
    assert 3 == solution.fib(4)
