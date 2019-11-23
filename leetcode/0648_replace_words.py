# -*- coding: utf-8 -*-


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.leaf = True

    def firstMatch(self, word):
        current = self.root
        for i, char in enumerate(word, 1):
            if char not in current.children:
                break
            current = current.children[char]
            if current.leaf:
                return word[:i]
        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        trie = Trie()
        for word in dict:
            trie.insert(word)

        result = []

        for word in sentence.split():
            result.append(trie.firstMatch(word))

        return ' '.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'the cat was rat by the bat' == solution.replaceWords(
        ['cat', 'bat', 'rat'], 'the cattle was rattled by the battery')
