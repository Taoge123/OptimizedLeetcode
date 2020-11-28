

class Solution:
    def stringMatching(self, words):
        res = set()
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j:
                    if word2.find(word1) != -1:
                        res.add(word1)
        return list(res)


