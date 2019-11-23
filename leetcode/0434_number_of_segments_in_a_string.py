# -*- coding: utf-8 -*-


class Solution(object):
    def countSegments(self, s):
        return len(s.split())


if __name__ == '__main__':
    solution = Solution()

    assert 5 == solution.countSegments('Hello, my name is John')
    assert 5 == solution.countSegments(' Hello, my name is John')
    assert 5 == solution.countSegments('Hello, my name is John ')
    assert 5 == solution.countSegments('Hello, my  name is John')
    assert 0 == solution.countSegments('')
