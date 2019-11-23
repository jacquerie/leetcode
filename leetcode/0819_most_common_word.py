# -*- coding: utf-8 -*-

import re
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z ]+', '', paragraph)

        words = Counter(paragraph.split())
        banned = set(banned)

        for word, _ in words.most_common():
            if word not in banned:
                return word


if __name__ == '__main__':
    solution = Solution()

    assert 'ball' == solution.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'])
