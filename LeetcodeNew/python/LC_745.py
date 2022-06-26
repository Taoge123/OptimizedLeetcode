import collections



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.children.get(char):
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, prefix):
        words = []
        node = self.root
        for char in prefix:
            if not node.children.get(char):
                return words
            node = node.children[char]
        self.findAllWords(node, prefix, words)
        return words

    def findAllWords(self, node, prefix, words):
        if node.is_word:
            words.append(prefix)
        for char, nextNode in node.children.items():
            self.findAllWords(nextNode, prefix + char, words)

# Tony's version
class Trie2:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, prefix):
        node = self.root
        res = set()
        path = ""
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
            path += ch
        self.dfs(node, path, res)
        return res

    def dfs(self, node, path, res):
        if node.isWord:
            res.add(path)

        for ch in node.children:
            self.dfs(node.children[ch], path + ch, res)


class WordFilter:
    def __init__(self, words):
        self.table = {word : i for i, word in enumerate(words)}

        self.trie1 = Trie()
        self.trie2 = Trie()
        self.cache1 = {}
        self.cache2 = {}

        for word in words:
            self.trie1.insert(word)
            self.trie2.insert(word[::-1])


    def f(self, prefix: str, suffix: str) -> int:

        if prefix in self.cache1:
            words1 = self.cache1[prefix]
        else:
            words1 = self.trie1.search(prefix)
            self.cache1[prefix] = words1

        if suffix in self.cache2:
            words2 = self.cache2[suffix]
        else:
            words2 = [word[::-1] for word in self.trie2.search(suffix[::-1])]
            self.cache2[suffix] = words2
        words = set(words1) & set(words2)
        res = -1
        for word in words:
            res = max(res, self.table[word])
        return res




"""
Store all the words corresponding to its prefixes and suffixes. For example, for two words bat and bar, the prefixes and suffixes dictionary will look as such:

# prefixes
{
  '': {'bat', 'bar'},
  'b': {'bat', 'bar'},
  'ba': {'bat', 'bar'},
  'bar': {'bar'},
  'bat': {'bat'},
}

# suffixes
{
  't': {'bat'},
  'at': {'bat'},
  'bat': {'bat'},
  'r': {'bar'},
  'ar': {'bar'},
  'bar': {'bar'},
}
f('b', 'at') => set intersection of {'bat', 'bar'} and {'bat'} => 'bat'.
"""

class WordFilter2:
    def __init__(self, words):
        self.prefixes = collections.defaultdict(set)
        self.suffixes = collections.defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix, suffix):
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight


