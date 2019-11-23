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

    def search(self, word):
        return self._search(word, self.root)

    def _search(self, word, current):
        for i, char in enumerate(word):
            if char == '.':
                for child in current.children:
                    if self._search(word[i + 1:], current.children[child]):
                        return True
                return False
            elif char not in current.children:
                return False
            current = current.children[char]
        return current.leaf


class WordDictionary(object):
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        return self.trie.search(word)


if __name__ == '__main__':
    obj = WordDictionary()

    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    assert not obj.search('pad')
    assert obj.search('bad')
    assert obj.search('.ad')
