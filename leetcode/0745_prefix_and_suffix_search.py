# -*- coding: utf-8 -*-

from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.leaf = True
        current.value = value

    def filter(self, prefix):
        node = self._walk(prefix)
        if node is None:
            return {-1}

        result = {-1}

        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.leaf:
                result.add(node.value)
            for child in node.children:
                queue.append(node.children[child])

        return result

    def _walk(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


class WordFilter:
    def __init__(self, words):
        self.prefixes = Trie()
        self.suffixes = Trie()
        for i, word in enumerate(words):
            self.prefixes.insert(word, i)
            self.suffixes.insert(word[::-1], i)

    def f(self, prefix, suffix):
        return max(self.prefixes.filter(prefix) & self.suffixes.filter(suffix[::-1]))


if __name__ == "__main__":
    obj = WordFilter(["apple"])

    assert 0 == obj.f("a", "e")
    assert -1 == obj.f("b", "")

    obj = WordFilter(["pop"])

    assert 0 == obj.f("", "op")
