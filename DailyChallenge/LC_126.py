



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
