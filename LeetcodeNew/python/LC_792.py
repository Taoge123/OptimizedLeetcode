
import collections

class Solution:
    def numMatchingSubseq(self, S, words):
        wordDict = collections.defaultdict(list)
        res = 0
        for word in words:
            wordDict[word[0]].append(word)

        for char in S:
            words_expecting_char = wordDict[char]
            wordDict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence!
                    res += 1
                else:
                    wordDict[word[1]].append(word[1:])
        return res



