"""
LCS - Longest Common Subsequence

https://leetcode.com/problems/uncrossed-lines/discuss/740453/Python3-Top-Down-DP-Pick-or-not-pick-element
"""

import functools


class Solution:
    def maxUncrossedLines(self, A, B) -> int:

        @functools.lru_cache(None)
        def dfs(i, j):

            if i >= len(A) or j >= len(B):
                return 0

            if A[i] == B[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)




