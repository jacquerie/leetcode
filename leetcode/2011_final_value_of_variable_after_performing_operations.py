# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum((1 if '+' in operation else -1) for operation in operations)


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.finalValueAfterOperations(['--X', 'X++', 'X++'])
    assert 3 == solution.finalValueAfterOperations(['++X', '++X', 'X++'])
    assert 0 == solution.finalValueAfterOperations(['X++', '++X', '--X', 'X--'])
