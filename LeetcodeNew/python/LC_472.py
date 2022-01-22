
"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""

import functools



class SolutionTonyMemo:
    def findAllConcatenatedWordsInADict(self, words):

        words = set(words)
        @functools.lru_cache()
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    return True

                if prefix in words and dfs(suffix):
                    return True
                # if suffix in words and dfs(prefix):
                #     return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res


class SolutionRika2:
    def findAllConcatenatedWordsInADict(self, words):
        cache = set(words)
        res = []

        @functools.lru_cache(None)
        def dfs(word, i):
            n = len(word)
            if i > n - 1:
                return True

            for j in range(i + 1, n + 1):
                if word[i:j] != word and (word[i:j] in cache):
                    if dfs(word, j):
                        return True
            return False

        for word in words:
            if not word:
                continue
            if dfs(word, 0):
                res.append(word)
        return res



class SolutionRika:
    def findAllConcatenatedWordsInADict(self, words):
        # similar to word break 1 and word break 2
        cache = set(words)

        res = []
        for word in words:
            if not word:
                continue
            if self.dfs(word, cache, 0, {}):
                res.append(word)
        return res

    def dfs(self, word, cache, i, memo):
        if i in memo:
            return memo[i]

        n = len(word)
        if i > n - 1:
            return True

        for j in range(i + 1, n + 1):
            if word[i:j] != word and (word[i:j] in cache):
                if self.dfs(word, cache, j, memo):
                    memo[i] = True
                    return memo[i]
        memo[i] = False
        return False


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord


class SolutionTrieTLE:
    def findAllConcatenatedWordsInADict(self, words):

        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        @functools.lru_cache()
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if self.trie.search(prefix) and self.trie.search(suffix):
                    return True
                if self.trie.search(prefix) and dfs(suffix):
                    return True
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res



class SolutionTonyTLE:
    def findAllConcatenatedWordsInADict(self, words):

        cache = set(words)
        res = []

        @functools.lru_cache(None)
        def dfs(word):
            n = len(word)
            for i in range(1, n):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in cache and suffix in cache:
                    return True
                if prefix in cache and dfs(suffix):
                    return True
                if suffix in cache and dfs(prefix):
                    return True
            return False

        for word in words:
            if dfs(word):
                res.append(word)
        return res




class SolutionTLE:
    def findAllConcatenatedWordsInADict(self, words):
        cache = set(words)
        res = []
        for word in words:
            if self.dfs(word, cache, res):
                res.append(word)
        return res

    def dfs(self, word, cache, res):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in cache and suffix in cache:
                return True
            if prefix in cache and self.dfs(suffix, cache, res):
                return True
            if suffix in cache and self.dfs(prefix, cache, res):
                return True

        return False


