import functools

class SolutionTony:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0

            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1) <= k




class SolutionTony2:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        return self.helper(s, 0, len(s) - 1, memo) <= k


    def helper(self, s, start, end, memo):
        if start >= end:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]

        if s[start] == s[end]:
            result = self.helper(s, start + 1, end - 1, memo)
        else:
            result = 1 + min(self.helper(s, start + 1, end, memo), self.helper(s, start, end - 1, memo))

        memo[(start, end)] = result
        return result


"""
KEY: The "order" of a reversed palidrome string is same with the original palidrome sting.

For instance: aba-> aba, abxyza -> azyxba.(still aba order)
The order of the palidrome string "aba" remains the same.
Therefore, leverageing LCS can help us find out the hidden palidrome string.
"""

class Solution2:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        t = s[::-1]
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)] # KEY: len + 1
        dp[0][0] = 0
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]: # index - 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(s) - dp[len(s)][len(t)] <= k



class Solution3:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if len(s) - k <= 1: return True
        import math
        dp = [[math.inf for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 0

        for m in range(1, len(s)):
            for i in range(len(s) - m):
                j = i + m
                if m == 1:
                    if s[i] == s[j]: dp[i][j] = 0
                    else: dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][-1] <= k




