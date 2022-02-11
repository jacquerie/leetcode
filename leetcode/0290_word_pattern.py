# -*- coding: utf-8 -*-


class Solution:
    def wordPattern(self, pattern, str):
        words = str.split()
        if len(pattern) != len(words):
            return False

        seen_chars, seen_words = {}, {}
        for char, word in zip(pattern, words):
            if char in seen_chars and seen_chars[char] != word:
                return False
            elif word in seen_words and seen_words[word] != char:
                return False
            seen_chars[char] = word
            seen_words[word] = char

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.wordPattern("abba", "dog cat cat dog")
    assert not solution.wordPattern("abba", "dog cat cat fish")
    assert not solution.wordPattern("aaaa", "dog cat cat dog")
    assert not solution.wordPattern("abba", "dog dog dog dog")
    assert not solution.wordPattern("abba", "dog cat cat")
    assert not solution.wordPattern("abb", "dog cat cat dog")
    assert not solution.wordPattern("", "beef")
