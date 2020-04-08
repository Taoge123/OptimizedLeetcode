import collections

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sentences = set()

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.buffer = ''
        self.table = collections.defaultdict(int)
        self.root = TrieNode()
        for s, t in zip(sentences, times):
            self.table[s] = t
            self.addSentence(s)
        self.tnode = self.root

    def input(self, c):
        ans = []
        if c != '#':
            self.buffer += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                ans = sorted(self.tnode.sentences, key=lambda x: (-self.table[x], x))[:3]
        else:
            self.table[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.root
        return ans

    def addSentence(self, sentence):
        current = self.root
        for letter in sentence:
            child = current.children.get(letter)
            if child is None:
                child = TrieNode()
                current.children[letter] = child
            current = child
            child.sentences.add(sentence)



class AutocompleteSystem2:
    def __init__(self, sentences, times):
        self.buffer = ''
        self.table = collections.defaultdict(int)
        self.root = TrieNode()
        for s, t in zip(sentences, times):
            self.table[s] = t
            self.addSentences(s)
        self.tnode = self.root

    def input(self, c: str):
        res = []
        if c != '#':
            self.buffer += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                res = sorted(self.tnode.sentences, key=lambda x: (-self.table[x], x))[:3]
        else:
            self.table[self.buffer] += 1
            self.addSentences(self.buffer)
            self.buffer = ''
            self.tnode = self.root
        return res

    def addSentences(self, sentence):
        node = self.root
        for char in sentence:
            if not node.children.get(char):
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences.add(sentence)





