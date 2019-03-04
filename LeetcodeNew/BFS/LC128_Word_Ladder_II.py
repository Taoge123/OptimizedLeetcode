"""
https://leetcode.com/problems/word-ladder-ii/discuss/174094/AC98-Clean-Python

The idea is pretty the same as word ladder I, but need to record the path,
and a few more considerations:

add two set: fwords, ewords to record words that hasn't been visited by front and back.
use dictionary front, back to map from <current_word> to <all_paths_to_this_word>,
there might be more than one path that can reach this word
combine all paths from front and back when find the result,
because we swap the front and end when length of front is bigger, so we need to:
look which path contains beginWord and use this path as a head
reverse another path before combine the two

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

class Solution2:
    def findLadders(self, begin, end, words):
        if end not in words: return []
        front, back = {begin: [[begin]]}, {end: [[end]]}
        fwords, ewords = set(words), set(words)
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                fwords, ewords = ewords, fwords
            hold = collections.defaultdict(list)
            toDel, res = set(), []
            for wd, pths in front.items():
                nxts = fwords & {wd[:i] + c + wd[i + 1:] \
                               for i in range(len(wd)) for c in string.ascii_lowercase}
                toDel |= nxts
                for w in nxts:
                    for pth in pths:
                        if w in back:
                            if pth[0] == begin:
                                res += [pth + bk[::-1] for bk in back[w]]
                            else:
                                res += [bk + pth[::-1] for bk in back[w]]
                        hold[w].append(pth + [w])
            if res: return res
            front = hold
            fwords -= toDel
        return []

class Solution2:
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

