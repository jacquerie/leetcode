# -*- coding: utf-8 -*-


class Solution:
    MORSE = {
        'a': '.-', 'b': '-...', 'c': '-.-.',
        'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-',
        'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..',
    }

    def transformation(self, word):
        return ''.join(self.MORSE[character] for character in word)

    def transformations(self, words):
        return [self.transformation(word) for word in words]

    def uniqueMorseRepresentations(self, words):
        return len(set(self.transformations(words)))


if __name__ == '__main__':
    solution = Solution()

    assert 2 == solution.uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg'])
