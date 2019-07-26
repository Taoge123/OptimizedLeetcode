"""
1) BFS starting at beginWord by transforming every letter to see
if the next word is in the wordList, if so, put in queue.
2) During BFS, maintain a graph of {word:nextWord} for all valid next wods
3) When a nextWord reaches endWord, do a backtracking DFS (pre-order traversal)
on the graph to get all paths.

"""

import collections
import string

class Solution:

    def findLadders(self, start, end, dic):
        dic.add(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:

                #Replace every string with all the lower case letter
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


class Solution2:
    def findLadders(self, beginWord, endWord, wordList):

        wordList = se
        t(wordList)
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


"""
The idea is pretty the same as word ladder I, 
but need to record the path, and a few more considerations:

add two set: fwords, ewords to record words that hasn't been visited by front and back.
use dictionary front, back to map from <current_word> to <all_paths_to_this_word>, 
there might be more than one path that can reach this word
combine all paths from front and back when find the result, 
because we swap the front and end when length of front is bigger, so we need to:
look which path contains beginWord and use this path as a head
reverse another path before combine the two

"""






