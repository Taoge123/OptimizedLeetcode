
"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

这是一道典型的DP题。凡是以数组形式出现的，求最大/最小/最多/最少而求非完整策略的题目，都不妨考虑一下DP算法的可能性。
最常见的状态数组就是设计成dp[i][j]，表示在[i,j]区间内的最优解，我们需要考察这个状态能否向下（即更小规模的区间）转移。

既然是判断dp[i][j]是否包含构成回文的subsequence，那么自然从两头往中间思考。
如果s[i]==s[j]的话，那么不要犹豫，这两个一定就是最长回文子序列中的成员。所以dp[i][j]=dp[i+1][j-1]+2

如果s[i]!=s[j]呢？这说明s[i]和s[j]两个中必然有一个不是最长回文子序列的成员（否则如果这两个都是的话，会造成最长回文子序列的两端不对称），
于是我们就可以排除一个。所以dp[i][j]=max(dp[i][j-1],dp[i+1][j]，这是一个很常见的处理方法。

有了以上的动态转移方程，就可以写DP算法了。注意虽然整体思路是从上往下分析，但DP算法的实现是从下往上的。
在这一题里，总体思想是先构建较短区间的dp值，慢慢扩展到较长区间的dp值。所以在最外层的循环里，我们控制一个len的变量，使其从到大变化。

此外，对于DP的初始条件，不难分析出dp[i][i]==1是必然的。然而，我们还需要铺垫所有的dp[i][i+1]，
目的是避免在动态转移的过程中出现dp[x][y], x>y的情况。

Follow Up:
如果用若干个一维数组代替这个N*N的二维数组，速度会有更大的提升。"""



class SolutionDFS:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        if len(s) == 1:
            return 1
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        if i == j:
            return 1

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]




class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        bbbab
        [1, 2, 3, 3, 4]
        [0, 1, 2, 2, 3]
        [0, 0, 1, 1, 3]
        [0, 0, 0, 1, 1]
        [0, 0, 0, 0, 1]
        """
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]





class SolutionWisdom:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][i] = 1

        for step in range(2, n + 1):
            for i in range(1, n - step + 2):
                j = i + step - 1
                # print(i, j)
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[1][n]








