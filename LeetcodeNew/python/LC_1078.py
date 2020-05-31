
class Solution:
    def findOcurrences(self, text: str, first: str, second: str):

        words = text.split(" ")
        res = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])

        return res



