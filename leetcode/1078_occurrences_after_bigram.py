# -*- coding: utf-8 -*-


class Solution(object):
    def findOcurrences(self, text, first, second):
        result = []

        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result


if __name__ == '__main__':
    solution = Solution()

    assert ['girl', 'student'] == solution.findOcurrences('alice is a good girl she is a good student', 'a', 'good')
    assert ['we', 'rock'] == solution.findOcurrences('we will we will rock you', 'we', 'will')
