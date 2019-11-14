
class Solution:
    def shortestWordDistance(self, words, word1, word2):

        res = float('inf')
        i1, i2 = float('-inf'), float('-inf')

        for i, word in enumerate(words):
            if word == word1:
                if word1 == word2:
                    res = min(res, i - i1)
                else:
                    res = min(res, i - i2)
                i1 = i
            elif word == word2:
                res = min(res, i - i1)
                i2 = i
        return res

words = ["practice", "makes", "perfect", "coding", "makes"]

word1 = "makes"
word2 = "makes"

a = Solution()
print(a.shortestWordDistance(words, word1, word2))







