# -*- coding: utf-8 -*-

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(word.capitalize() if len(word) > 2 else word.lower() for word in title.split())


if __name__ == '__main__':
    solution = Solution()

    assert 'Capitalize The Title' == solution.capitalizeTitle('capiTalIze tHe titLe')
    assert 'First Letter of Each Word' == solution.capitalizeTitle('First leTTeR of EACH Word')
    assert 'i Love Leetcode' == solution.capitalizeTitle('i lOve leetcode')
