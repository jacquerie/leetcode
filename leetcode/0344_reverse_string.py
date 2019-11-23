# -*- coding: utf-8 -*-


class Solution(object):
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert 'olleh' == solution.reverseString('hello')
    assert 'amanaP :lanac a ,nalp a ,nam A' == solution.\
        reverseString('A man, a plan, a canal: Panama')
