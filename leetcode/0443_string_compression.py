# -*- coding: utf-8 -*-

import itertools


class Solution(object):
    def compress(self, chars):
        result = []
        for char, group in itertools.groupby(chars):
            result.append(char)
            length = len(list(group))
            if length > 1:
                result.append(str(length))

        chars[:] = list(''.join(result))
        return len(chars)


if __name__ == '__main__':
    solution = Solution()

    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']

    assert 6 == solution.compress(chars)
    assert ['a', '2', 'b', '2', 'c', '3'] == chars

    chars = ['a']

    assert 1 == solution.compress(chars)
    assert ['a'] == chars

    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

    assert 4 == solution.compress(chars)
    assert ['a', 'b', '1', '2'] == chars
