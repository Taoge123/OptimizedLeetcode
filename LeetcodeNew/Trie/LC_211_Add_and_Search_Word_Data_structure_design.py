
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

import collections

class WordDictionary1:
    def __init__(self):
        self.word_dict = collections.defaultdict(set)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].add(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary2:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])


class TrieNode:

    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary3:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word


class WordDictionary4:
    def __init__(self):
        self.len2words = collections.defaultdict(list)

    def addWord(self, word):
        self.len2words[len(word)].append(word)

    def search(self, word):
        words = self.len2words[len(word)]
        for i, char in enumerate(word):
            words = [w for w in words if char in ('.', w[i])]
            if not words: return False
        return True



class WordDictionary5:
    def __init__(self):
        self.dic = collections.defaultdict(list)
    def addWord(self, word):
        self.dic[len(word)].append(word)
    def search(self, word):
        for stored_word in self.dic[len(word)]:
            if all(word[i] == stored_word[i] for i in range(len(word)) if word[i] != "."): return True
        return False


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_leaf = False


class WordDictionary6:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word):
        return self.helper(word, self.root)

    def helper(self, word, node):
        if len(word) == 0:
            return node.is_leaf
        first = word[0]
        if first == ".":
            for key in node.children:
                # return true if any was true
                if self.helper(word[1:], node.children[key]):
                    return True
        else:
            if first not in node.children:
                return False
            return self.helper(word[1:], node.children[first])
        return False


