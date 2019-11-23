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
        return self._search(word, self.root, False)

    def _search(self, word, current, error):
        for i, char in enumerate(word):
            if not error:
                for child in current.children:
                    if self._search(word[i + 1:], current.children[child], char != child):
                        return True
                return False
            elif error and char not in current.children:
                return False
            current = current.children[char]
        return current.leaf and error


class MagicDictionary(object):
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dict):
        for word in dict:
            self.trie.insert(word)

    def search(self, word):
        return self.trie.search(word)


if __name__ == '__main__':
    obj = MagicDictionary()

    obj.buildDict(['hello', 'leetcode'])
    assert not obj.search('hello')
    assert obj.search('hhllo')
    assert not obj.search('hllo')
    assert not obj.search('leetcoded')

    obj.buildDict(['hello', 'hallo', 'hell', 'leetcoded'])
    assert obj.search('hello')
    assert obj.search('hhllo')
    assert not obj.search('hllo')
    assert not obj.search('leetcoded')
