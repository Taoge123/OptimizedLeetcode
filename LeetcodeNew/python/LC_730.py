"""
https://www.youtube.com/watch?v=UjiFFYU3EKM
really hard
"""

import functools


class SolutionTD:
    def countPalindromicSubsequences(self, S):
        @functools.lru_cache(None)
        def dfs(s):
            res = 0
            for ch in set(s):
                left = s.find(ch)
                right = s.rfind(ch)
                if left == right:
                    res += 1
                else:
                    res += dfs(s[left + 1:right]) + 2
            return res

        return dfs(S) % 1000000007



class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 10 ** 9 + 7

        def count(S, i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if self.table[i][j]:
                return self.table[i][j]

            if S[i] == S[j]:
                res = count(S, i + 1, j - 1) * 2
                left = i + 1
                right = j - 1
                while left <= right and S[left] != S[i]:
                    left += 1
                while left <= right and S[right] != S[i]:
                    right -= 1
                if left > right:
                    res += 2
                elif left == right:
                    res += 1
                else:
                    res -= count(S, left + 1, right - 1)
            else:
                res = count(S, i + 1, j) + count(S, i, j - 1) - + count(S, i + 1, j - 1)

            self.table[i][j] = res % mod
            return self.table[i][j]

        n = len(S)
        self.table = [[None for i in range(n)] for j in range(n)]
        return count(S, 0, n - 1)






