# -*- coding: utf-8 -*-

VOWELS = 'AEIOUaeiou'


class Solution(object):
    def toGoatLatin(self, S):
        result = []

        for i, word in enumerate(S.split(), 1):
            result.append(self._toGoatLatin(word) + ('a' * i))

        return ' '.join(result)

    def _toGoatLatin(self, word):
        if word[0] in VOWELS:
            return word + 'ma'
        else:
            return word[1:] + word[0] + 'ma'


if __name__ == '__main__':
    solution = Solution()

    assert 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa' == solution.toGoatLatin('I speak Goat Latin')
