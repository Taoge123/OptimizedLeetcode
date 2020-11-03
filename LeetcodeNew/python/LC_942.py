
class Solution:
    def diStringMatch(self, S: str):
        low, high = 0, len(S)
        res = []
        for ch in S:
            if ch == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        return res + [low]



