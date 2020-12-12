
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        res = []
        for i in range( n +1):
            if sequence.count(word * i ) >0:
                res.append(i)
        if len(res) > 0:
            return max(res)
        else:
            return 0


