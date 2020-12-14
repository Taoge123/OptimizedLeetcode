
import collections


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

    def search(self, queries):
        node = self.root
        for q in queries:
            if q in node.children:
                node = node.children[q]
                if node.isWord:
                    return True
            else:
                return False




class StreamChecker2:
    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.queries = collections.deque()

    def query(self, letter: str) -> bool:
        self.queries.appendleft(letter)
        if len(self.queries) > 2000:
            self.queries.pop()
        return self.trie.search(self.queries)




class StreamChecker:
    def __init__(self, words):
        self.s = ''
        self.table = collections.defaultdict(set)
        for word in words:
            self.table[word[-1]].add(word)


    def query(self, letter: str) -> bool:
        self.s += letter
        res = False
        for word in self.table[letter]:
            if self.s.endswith(word):
                return True
        return False
        # return any(self.s.endswith(word) for word in self.table[letter])




