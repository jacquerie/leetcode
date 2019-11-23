# -*- coding: utf-8 -*-


class Solution(object):

    VOWELS = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

    def reverseVowels(self, s):
        result = list(s)

        i, j = 0, len(s) - 1
        while i <= j:
            if result[i] not in self.VOWELS:
                i += 1
            elif result[j] not in self.VOWELS:
                j -= 1
            else:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'holle' == solution.reverseVowels('hello')
    assert 'Aa' == solution.reverseVowels('aA')
    assert 'EO' == solution.reverseVowels('OE')
