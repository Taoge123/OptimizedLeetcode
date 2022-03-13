"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

import collections


class Solution:
    def wordSquares(self, words):
        res = []
        table = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                table[word[:i]].add(word)
        for word in words:
            self.dfs(table, word, 1, [], res)
        return res

    def dfs(self, table, word, index, path, res):
        path.append(word)
        if index == len(word):
            res.append(path[:])
        else:
            prefix = "".join(path[i][index] for i in range(index))
            for word in table[prefix]:
                self.dfs(table, word, index + 1, path, res)
        path.pop()




class SolutionRika:
    def wordSquares(self, words):
        if len(words) == 1:
            return words[0]

        # step1: build graph
        graph = collections.defaultdict(set)
        for word in words:
            for i in range(1, len(word)):
                prefix = word[:i]
                graph[prefix].add(word)

        # step2: for loop each start word, do dfs
        self.res = []
        for word in words:
            self.dfs(graph, word, 1, [word])

        return self.res

    def dfs(self, graph, word, pos, path):

        if pos == len(word):
            self.res.append(path[:])
            return
        prefix = ''
        for string in path:
            prefix += string[pos]

        if prefix in graph:
            for nextword in graph[prefix]:
                self.dfs(graph, word, pos + 1, path + [nextword])


"""
ie, when index == 2:
LEA will be the prefix, then we will search LEA in table and continue to backtrack

[[ "w a L l",
   "a r E a",
   "l e A d",
   "l a d y"],


["ball","area","lead","lady"]]

"""


class SolutionTrie:
    def wordSquares(self, words):
        self.N = len(words[0])
        self.trie = self.buildTrie(words)
        self.ans = []
        for w in words:
            self.buildSquare([w])
        return self.ans

    def buildTrie(self, words):
        trie = {}
        for w in words:
            node = trie
            for char in w:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = w
        return trie

    def buildSquare(self, square):
        cur_len = len(square)
        if cur_len == self.N:
            self.ans.append(square)
            return

        cur_sq_prefix = list(zip(*square))
        cur_prefix = ''.join(cur_sq_prefix[cur_len])
        self.candidates = []
        self.searchPrefix(self.trie, cur_prefix)
        for w in self.candidates:
            self.buildSquare(square + [w])

    def searchPrefix(self, node, prefix):
        if '#' in node:
            self.candidates.append(node['#'])
            return

        for char in prefix:
            if char not in node:
                return
            node = node[char]

        for char in node:
            self.searchPrefix(node[char], '')





words = ["area","lead","wall","lady","ball"]
a = Solution()
print(a.wordSquares(words))



