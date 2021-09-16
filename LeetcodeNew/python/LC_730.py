"""
https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109510/Python-DP%2BDFS-O(n2)-with-Explanations

https://www.youtube.com/watch?v=UjiFFYU3EKM
really hard

First of all, I compute when 'a' appears first (index i) and last (index j) in the segment I am considering. Then it breaks down into two cases:

If i == j. There is only one 'a' in the segment. So the answer is 1.
If i != j. The possible palindromes are 'a', 'aa', and 'a*a' where '*' stands for any palindromes contained in S[i+1:j]. The answer would be DFS(i+1,j) + 2. Since I want to avoid repetitive computation, I write cache(i+1,j) + 2 instead.
The worst case time complexity is O(n^2). The best case time complexity is O(n).
"""

import functools


class Solution0:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 1000000007

        @functools.lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            # if i == j:
            #     return 1
            res = 0
            for ch in set(S[i:j + 1]):
                left = S.find(ch, i, j + 1)
                right = S.rfind(ch, i, j + 1)
                if left == right:
                    res += 1
                else:
                    res += dfs(left + 1, right - 1) + 2

            return res % mod

        return dfs(0, len(S) - 1)



class SolutionTD1:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 1000000007

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            res = 0
            for ch in set(S[i:j]):
                left = S.find(ch, i, j)
                right = S.rfind(ch, i, j)
                if left == right:
                    res += 1
                else:
                    res += dfs(left + 1, right) + 2

            return res % mod

        return dfs(0, len(S))



class SolutionTony:
    def countPalindromicSubsequences(self, S):
        memo = {}
        return self.dfs(S, memo) % 1000000007

    def dfs(self, s, memo):
        if s in memo:
            return memo[s]
        res = 0
        for ch in set(s):
            i = s.find(ch)
            j = s.rfind(ch)
            if i == j:
                res += 1
            else:
                res += self.dfs(s[i + 1:j], memo) + 2
        memo[s] = res
        return res


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






