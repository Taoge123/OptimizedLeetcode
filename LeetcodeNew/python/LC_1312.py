
from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            else:
                return min(dp(i + 1, j), dp(i, j - 1)) + 1

        return dp(0, n - 1)



"""
解法2：
另一种更容易理解和想到的方法是区间型DP：定义dp[i][j]表示区间s[i:j]变成回文串最少需要多少添加多少字符。状态转移方程很容易理解：

if (s[i]==s[j])  
  dp[i][j]=dp[i+1][j-1]; 
else 
  dp[i][j] = min(dp[i+1][j]+1,dp[i][j-1]+1) 
  // 前者表示让s[i+1:j]已经成为回文串，再在s[j]后添加一个与s[i]相同的字符使得s[i:j]变成回文串
  // 前者表示让s[i:j-1]已经成为回文串，再在s[i]前添加一个与s[j]相同的字符使得s[i:j]变成回文串"""


class Solution2:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for step in range(n):
            for i in range(n - step):
                j = i + step
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]

"""
解法1：
第一种方法是：我们将原数列s逆序得到t。本题的答案等同于求这两个字符串的shortest common supersequence (SCS)。

这个转换其实并不容易理解。我们只能大概地有一种直观的感受：因为s和t是逆序关系，s最后一个字符等于t的第一个字符，
应该让s放置于t的前面，尽可能地重合s的尾部和t的头部来提高字符重用的利用效率。所以最终s和t的SCS应该是个回文串。
既然SCS的第一个S是shortest的意思，那么这个SCS就是通过s可以得到的最短的回文串。

这么转换之后，本题就是1092.Shortest-Common-Supersequence.
"""
import functools

class SolutionTony1:
    def minInsertions(self, s: str) -> int:

        @functools.lru_cache(None)
        def dfs(i, j):
            if j - i < 1:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1)



class SolutionTony2:
    def minInsertions(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j - i < 1:
            return 0
        if s[i] == s[j]:
            memo[(i, j)] = self.dfs(s, i + 1, j - 1, memo)
        else:
            memo[(i, j)] = min(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo)) + 1

        return memo[(i, j)]




class Solution1:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        t = s[::-1]

        for i in range(1, n + 1):
            dp[i][0] = i
            dp[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[n][n] - n


