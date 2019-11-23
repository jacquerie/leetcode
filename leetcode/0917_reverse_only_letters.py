# -*- coding: utf-8 -*-

import string


class Solution(object):
    def reverseOnlyLetters(self, S):
        result = list(S)

        i, j = 0, len(S) - 1
        while i <= j:
            if result[i] not in string.ascii_letters:
                i += 1
            elif result[j] not in string.ascii_letters:
                j -= 1
            else:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'dc-ba' == solution.reverseOnlyLetters('ab-cd')
    assert 'j-Ih-gfE-dCba' == solution.reverseOnlyLetters('a-bC-dEf-ghIj')
    assert 'Qedo1ct-eeLg=ntse-T!' == solution.reverseOnlyLetters('Test1ng-Leet=code-Q!')
