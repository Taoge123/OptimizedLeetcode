
class Solution:
    def minCut(self, s: str) -> int:

        f = [-1] + [len(s ) -1 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range( i +1 ,len(s ) +1):
                if s[i:j] == s[i:j][::-1]:
                    f[j] = min(f[j], f[i] + 1)
        return f[-1]




