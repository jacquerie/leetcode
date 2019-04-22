# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        new_letters = list(sorted(set(letters + [target])))
        double_new_letters = ''.join(new_letters * 2)

        return double_new_letters[double_new_letters.find(target) + 1]


if __name__ == '__main__':
    solution = Solution()

    assert 'c' == solution.nextGreatestLetter(['c', 'f', 'j'], 'a')
    assert 'f' == solution.nextGreatestLetter(['c', 'f', 'j'], 'c')
    assert 'f' == solution.nextGreatestLetter(['c', 'f', 'j'], 'd')
    assert 'j' == solution.nextGreatestLetter(['c', 'f', 'j'], 'g')
    assert 'c' == solution.nextGreatestLetter(['c', 'f', 'j'], 'j')
