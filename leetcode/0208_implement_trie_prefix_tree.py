# -*- coding: utf-8 -*-


class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie:
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
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.leaf

    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    obj = Trie()

    obj.insert("apple")
    assert obj.search("apple")
    assert not obj.search("app")
    assert obj.startsWith("app")
    obj.insert("app")
    assert obj.search("app")
