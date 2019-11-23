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

    def findMaximumXOR(self, word):
        current, result = self.root, 0
        for i, char in enumerate(word, 1):
            if char == '0' and '1' in current.children:
                current, result = current.children['1'], result + 2 ** (32 - i)
            elif char == '1' and '0' in current.children:
                current, result = current.children['0'], result + 2 ** (32 - i)
            else:
                current = current.children[char]
        return result


class Solution(object):
    def findMaximumXOR(self, nums):
        trie = Trie()
        for num in nums:
            trie.insert(format(num, '032b'))

        result = 0
        for num in nums:
            result = max(result, trie.findMaximumXOR(format(num, '032b')))
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 28 == solution.findMaximumXOR([3, 10, 5, 25, 2, 8])
