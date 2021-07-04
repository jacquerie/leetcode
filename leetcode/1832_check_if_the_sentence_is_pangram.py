# -*- coding: utf-8 -*-

import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return all(letter in sentence for letter in string.ascii_lowercase)


if __name__ == '__main__':
    solution = Solution()

    assert solution.checkIfPangram('thequickbrownfoxjumpsoverthelazydog')
    assert not solution.checkIfPangram('leetcode')
