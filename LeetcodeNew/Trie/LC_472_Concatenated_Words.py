
"""
Given a list of words (without duplicates),
please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words):

        ans = []
        self.wordSet = set(words)
        for word in words:
            self.wordSet.remove(word)
            if self.search(word):
                ans.append(word)
            self.wordSet.add(word)
        return ans

    def search(self, word):
        if word in self.wordSet:
            return True
        for idx in range(1, len(word)):
            if word[:idx] in self.wordSet and self.search(word[idx:]):
                return True
        return False



class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord

class Solution2:
    def findAllConcatenatedWordsInADict(self, words):
        self.trie = Trie()
        ans = []
        for word in words:
            self.trie.insert(word)
        for word in words:
            if self.search(word):
                ans.append(word)
        return ans

    def search(self, word):
        node = self.trie.root
        for idx, letter in enumerate(word):
            node = node.children.get(letter)
            if node is None:
                return False
            suffix = word[idx+1:]
            if node.isWord and (self.trie.search(suffix) or self.search(suffix)):
                return True
        return False










