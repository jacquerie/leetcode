# -*- coding: utf-8 -*-


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.isPrefixOfWord('i love eating burger', 'burg')
    assert 2 == solution.isPrefixOfWord('this problem is an easy problem', 'pro')
    assert - 1 == solution.isPrefixOfWord('i am tired', 'you')
    assert 4 == solution.isPrefixOfWord('i use triple pillow', 'pill')
