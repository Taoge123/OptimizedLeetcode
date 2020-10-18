"""
0 1 2 3 4 5 6 7 8 9 10 11
l o v e l e r t c o d  e
"""

class Solution:
    def shortestToChar(self, S: str, C: str):
        n = len(S)
        res = [0] * n
        pos = -n

        for i in range(n):
            if S[i] == C:
                pos = i
            res[i] = i - pos

        for i in range(n - 1, -1, -1):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))

        return res


