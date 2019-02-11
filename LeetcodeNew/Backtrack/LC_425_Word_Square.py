import collections

"""
I try every word for the first row. For each of them, 
try every fitting word for the second row. And so on. 
The first few rows determine the first few columns and thus determine how the next row's word must start. 
For example:

wall      Try words      wall                     wall                      wall
a...   => starting  =>   area      Try words      area                      area
l...      with "a"       le..   => starting  =>   lead      Try words       lead
l...                     la..      with "le"      lad.   => starting   =>   lady
                                                            with "lad"
"""
#This is python 2.7
class Solution:
    def wordSquares(self, words):
        n = len(words[0])
        fulls = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                fulls[word[:i]].append(word)

        def build(square):
            if len(square) == n:
                squares.append(square)
                return
            print(square)
            for word in fulls[''.join(zip(*square)[len(square)])]:
                build(square + [word])

        squares = []
        for word in words:
            build([word])
        return squares


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(list)


class Solution2(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        node = self.root
        for word in words:
            for i in range(len(words[0])):
                node.children[word[:i]].append(word)

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        # runtime: 904ms

        def buildSquare(square):
            node = self.root
            if len(square) == len(words[0]):
                res.append(square)
                return
            [buildSquare(square + [word]) for word in node.children[''.join(zip(*square)[len(square)])]]

        res = []
        self.insert(words)
        for word in words:
            buildSquare([word])
        return res
#
#
# a = Solution()
# aa = a.wordSquares(["area","lead","wall","lady","ball"])
#
# print(aa)

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        # collect all words in this subtrie
        def gather_trie(trie, res, item):
            if (not trie):
                if (len(item) > 0):
                    res.append(item)
                return

            for c in trie:
                gather_trie(trie[c], res, item + c)

        # add word to trie
        def add_word(trie, word, start):
            if (start == len(word)):
                return
            if (word[start] not in trie):
                trie[word[start]] = {}
            add_word(trie[word[start]], word, start + 1)

        # build trie; dict of dicts
        # don't worry about leaf markers because all words are of same length
        # and no duplicates
        def build_trie(words):
            trie = {}
            for word in words:
                add_word(trie, word, 0)
            return trie

        # gather all possible words with given prefix
        def get_words(trie, prefix):
            for c in prefix:
                if (c not in trie):
                    return []  # return empty if prefix not found
                trie = trie[c]
            # traverse this subtrie to gather words
            res = []
            gather_trie(trie, res, prefix)
            return res

        # search through backtracking
        def backtrack(trie, res, item, chari, l, prefix):
            cands = get_words(trie, prefix)
            for cand in cands:
                if (len(item) == l - 1):
                    res.append(list(item + [cand]))
                    continue
                # construct new prefix for next word search
                newprefix = ''.join([word[chari + 1] for word in (item + [cand])])
                backtrack(trie, res, item + [cand], chari + 1, l, newprefix)

        l = len(words)
        if (l == 0):
            return [[]]
        trie = build_trie(words)
        res = []
        backtrack(trie, res, [], 0, len(words[0]), '')
        return res


"""
Read and learned from other posts. Basic idea is use trie + backtrack. 
Trie related functions are 'build_trie', 'add_str', 'search_str'. 
And backtrack function is just 'find_word_squares'. 
Hope it's more understandable. Leave comments if you have any thoughts.

"""


class Solution2(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = {}
        self.build_trie(words, trie)

        size = len(words[0])

        result = []
        self.find_word_squares(trie, size, [], result)
        return result

    def build_trie(self, words, trie):
        for word in words:
            self.add_str(word, trie)

    def add_str(self, string, root):
        node = root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = string

    def search_prefix(self, node, prefix, candidates):
        if '#' in node:
            candidates.append(node['#'])
            return

        for letter in prefix:
            if letter not in node:
                return
            node = node[letter]

        for letter in node:
            self.search_prefix(node[letter], '', candidates)

    def find_word_squares(self, trie, size, cur, result):
        if len(cur) == size:
            result.append(cur[:])
            return

        candidates = []
        prefix = ''.join([string[len(cur)] for string in cur])
        self.search_prefix(trie, prefix, candidates)

        for candidate in candidates:
            self.find_word_squares(trie, size, cur + [candidate], result)


#Append next prefix if row[i] == col[i] in arr

class Solution3:
    def wordSquares(self, words):
        #build prefix table, key is [:i] and values are all words with this prefix
        prefix, res = collections.defaultdict(set), []
        for word in words:
            for i in range(len(word)):
                prefix[word[:i + 1]].add(word)
                # print(prefix)
        #Once index reach the last column, then we got the result
        #   i
        # w a l l
        # a r e a
        # l e a d
        # l a d y
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                #when we only have wall, row will only take the ith column and merged it as word
                for word in prefix["".join(row[i] for row in arr)]:
                    dfs(i + 1, arr + [word])
        for word in words:
            dfs(1, [word])
        return res



"""
Key idea: use a list containing k-1 hashmaps, k is the length of words.
Example:
words = ["abc", "ade", "abd", "adf"]
list of hash maps = [{"a": ["abc","ade","abd", "adf"]}, {"ab":["abc", "abd"], "ad":["ade","adf"]}]
The data structure is like a trie, but trade off space for time. 
It is feasible considering the word length is between 1 and 5.
"""

class Trie:
    def __init__(self, words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = dict()
            if '#' not in node:
                node['#'] = []
            node['#'].append(word)
            node = node[char]

class Solution4(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = Trie(words)
        squares = []
        square = []

        def dfs(idx):
            if square and idx == len(square[0]):
                squares.append(square[:])
                return
            node = trie.root
            for word in square:
                char = word[idx]
                if char not in node:
                    return
                node = node[char]
            for word in node['#']:
                square.append(word)
                dfs(idx + 1)
                square.pop()

        dfs(0)
        return squares


a = Solution4()
aa = a.wordSquares(["area","lead","wall","lady","ball"])

print(aa)
