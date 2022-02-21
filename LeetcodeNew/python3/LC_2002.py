"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/discuss/1463790/Backtracking-or-explained-solution-or-c%2B%2B

"""


import functools

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def isPal(word):
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True

        @functools.lru_cache(None)
        def dfs(i, w1, w2):
            if i >= n:
                if isPal(w1) and isPal(w2):
                    self.res = max(self.res, len(w1) * len(w2))
                return

            dfs(i + 1, w1, w2)
            dfs(i + 1, w1 + s[i], w2)
            dfs(i + 1, w1, w2 + s[i])

        self.res = 0
        dfs(0, "", "")
        return self.res




class SolutionRika:
    def maxProduct(self, s: str) -> int:
        memo = {}
        n = len(s)
        for i in range(1, 1 << n):
            subsequences = ""
            for j in range(n):
                if i >> j & 1 == 1:
                    subsequences += s[j]
            if subsequences == subsequences[::-1]:
                memo[i] = len(subsequences)

        res = 0
        for s1, sz1 in memo.items():
            for s2, sz2 in memo.items():
                if s1 & s2 == 0:
                    res = max(res, sz1 * sz2)
        return res