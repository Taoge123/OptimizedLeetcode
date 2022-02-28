"""
https://leetcode.com/problems/word-ladder-ii/discuss/735921/Python-or-DFS-%2B-Backtrack-or-With-explanation


"""


import collections
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        #we dont need visited since we will remove the newLayer.values() for the words we have processed
        wordList = set(wordList)
        res = []
        lowercase = string.ascii_lowercase
        #layer is similar to queue in 127
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    for i in layer[word]:
                        res.append(i)
                else:
                    for i in range(len(word)):
                        for char in lowercase:
                            newWord = word[:i] + char + word[i+1:]
                            if newWord in wordList:
                                for valList in layer[word]:
                                    # print(newWord, valList + [newWord])
                                    newLayer[newWord].append(valList + [newWord])

            wordList -= set(newLayer.keys())
            layer = newLayer
        return res


class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        # we dont need visited since we will remove the newLayer.values() for the words we have processed
        wordList = set(wordList)
        res = []
        lowercase = string.ascii_lowercase
        # layer is similar to queue in 127
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                for i in range(len(word)):
                    for char in lowercase:
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            for valList in layer[word]:
                                # print(newWord, valList + [newWord])
                                newLayer[newWord].append(valList + [newWord])

            if endWord in newLayer:
                return newLayer[endWord]
            wordList -= set(newLayer.keys())
            layer = newLayer
        return res


class SolutionTwoDirectional:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return []

        # we dont need visited since we will remove the newLayer.values() for the words we have processed
        wordList = set(wordList)
        lowercase = string.ascii_lowercase

        layer = collections.defaultdict(list)
        another_layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        another_layer[endWord] = [[endWord]]
        ans = []

        while layer:
            newLayer = collections.defaultdict(list)
            wordList -= set(layer.keys())

            for word in layer:
                if word in another_layer:
                    for lst1 in layer[word]:
                        for lst2 in another_layer[word]:
                            ans.append(lst1 + lst2[:-1][::-1])
                else:
                    for i in range(len(word)):
                        for char in lowercase:
                            newWord = word[:i] + char + word[i + 1:]
                            if newWord in wordList:
                                for valList in layer[word]:
                                    newLayer[newWord].append(valList + [newWord])

            if ans:
                if ans[0][0] == endWord:
                    for lst in ans:
                        lst.reverse()
                return ans

            layer = newLayer
            if len(layer) > len(another_layer):
                layer, another_layer = another_layer, layer



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
a = Solution()
print(a.findLadders(beginWord, endWord, wordList))
