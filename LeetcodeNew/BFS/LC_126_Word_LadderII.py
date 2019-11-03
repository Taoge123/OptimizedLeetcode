"""
1) BFS starting at beginWord by transforming every letter to see
if the next word is in the wordList, if so, put in queue.
2) During BFS, maintain a graph of {word:nextWord} for all valid next wods
3) When a nextWord reaches endWord, do a backtracking DFS (pre-order traversal)
on the graph to get all paths.

"""


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
import collections, string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordList = set(wordList)
        res = []
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        lowercase = string.ascii_lowercase

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    for i in layer[word]:
                        res.append(i)
                else:
                    for i in range(len(word)):
                        for char in lowercase:
                            newWord = word[:i] + char + word[i + 1:]
                            if newWord in wordList:
                                for j in layer[word]:
                                    newLayer[newWord].append(j + [newWord])

            wordList -= set(newLayer.keys())
            layer = newLayer
        return res







