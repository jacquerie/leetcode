# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.strStr('hello', 'll')
    assert -1 == solution.strStr('aaaaa', 'bba')
    assert 0 == solution.strStr('aaaaa', '')
