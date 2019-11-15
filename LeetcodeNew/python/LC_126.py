import collections
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):

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
                            newWord = word[:i] + char + word[ i +1:]
                            if newWord in wordList:
                                for j in layer[word]:
                                    newLayer[newWord].append(j + [newWord])

            wordList -= set(newLayer.keys())
            layer = newLayer
        return res





