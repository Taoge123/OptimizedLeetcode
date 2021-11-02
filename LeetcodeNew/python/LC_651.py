import functools


"""
https://leetcode.com/problems/4-keys-keyboard/discuss/246227/intuitive-python-topdown-with-memo
"""
class Solution:
    def maxA(self, n):
        @functools.lru_cache(None)
        def dfs(already, copied, step):
            if step == n:
                return already
            choiceA, choiceV, choiceACV = 0, 0, 0
            if copied == 0:
                choiceA = dfs(already+1, copied, step+1)
            if copied > 0:
                choiceV = dfs(already+copied, copied, step+1)
            if step + 3 <= n:
                choiceACV = dfs(already*2, already, step+3)
            return max(choiceA,choiceV,choiceACV)
        return dfs(1, 0, 1)




class Solution:
    def maxA(self, N: int) -> int:
        dp = [0] * (N + 1)
        for i in range(N + 1):
            dp[i] = i
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[-1]



class Solution2:
    def maxA(self, N):
        dp = [i for i in range(N+1)]
        for i in range(7, N+1):
            dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

        return f[N]

