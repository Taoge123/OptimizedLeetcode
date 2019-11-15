
class Solution:
    def findRepeatedDnaSequences(self, s):

        visited = set()
        res = set()
        for i in range(len(s) - 9):
            word = s[i:i + 10]
            if word in visited:
                res.add(word)
            else:
                visited.add(word)
        return list(res)





