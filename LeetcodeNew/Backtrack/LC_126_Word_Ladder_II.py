"""
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList,
therefore no possible transformation.

"""

import collections
import string

class Solution:
# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return a list of lists of string
    def findLadders(self, start, end, dic):
        dic.add(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res


"""
If we know source and destination, 
we can build the word tree by going forward in one direction and backwards in the other. 
We stop when we have found that a word in the next level of BFS is in the other level, 
but first we need to update the tree for the words in the current level.

Then we build the result by doing a DFS on the tree constructed by the BFS.

The difference between normal and double BFS is that the search changes 
from O(k^d) to O(k^(d/2) + k^(d/2)). 
Same complexity class, right? Yeah, 
tell it to the Facebook guys that have to search in graphs with hundreds of
thousands of nodes.

"""


class Solution(object):

    # Solution using double BFS

    def findLadders(self, begin, end, words_list):

        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]
                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev: return False
            if len(this_lev) > len(oth_lev):
                return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index + 1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)

        tree, path, paths = collections.defaultdict(list), [begin], []
        is_found = bfs_level(set([begin]), set([end]), tree, True, words_list)
        return construct_paths(begin, end, tree)


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res




