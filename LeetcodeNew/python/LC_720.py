
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True
        node.word = word

    def bfs(self):
        q = collections.deque([self.root])
        res = ''
        while q:
            cur = q.popleft()
            for n in cur.children.values():
                if n.isEnd:
                    q.append(n)
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res


class SolutionTrie:
    def longestWord(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.bfs()



class Solution2:
    def longestWord(self, words) -> str:
        words.sort()
        words_set = set([''])
        res = ""
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(res):
                    res = word
        return res
