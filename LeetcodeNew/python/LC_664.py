"""
拿到这题，我会考虑这样一个问题，最基本款的打印方案是什么？当然是一个字一个字地打印，也就是打印N次。

然后我想，题目中的打印方式会带来什么优势？我会想到这样一个例子：a X X X X a X X X X。如果我们在打印第一个a的时候，
顺便把整个字符串都打印上a，那么字符串中间的那个a就占了便宜。我们接下来只需要考虑处理两个更小的区间X X X X怎么打印就行了。也就是说，此时动态转移方程呼之欲出：

设计动态转移方程dp[i][j]，表示打印以s[i]开始、s[j]结尾的子串，需要最少的turns。

dp[i][j] = 1+dp[i+1][j]  //基本款
dp[i][j] = min { dp[i][k-1] + dp[k+1][j] }  for s[k]==s[i]
注意，如果k+1>j，那么dp[k+1][j]的值默认为0.

如果你有兴趣，会更深入地想，在处理dp[i][j]的时候，为什么首先一定是先从i位置开始打印一串s[i]的字符呢？
为什么不是先打印其他地方的字符，再从i位置开始打印一串s[i]的字符呢？原因是s[i]不能依靠打印其他字符时被“捎带”上，
必须老老实实在i的位置单独打印。与其在i位置单独打一个s[i]，肯定不如顺便直接打出一串s[i]。
想到这点的话，如果我们先打印了其他地方的XXXX的字符、再不幸被这串s[i]覆盖的话，显然效率肯定低，
不如索性第一步就从i位置开始打印一串s[i]的字符。这就是以上思想为什么总是我们在处理dp[i][j]时，总是考虑首先要打印一串s[i]的原因。

因为根据dp[i][j]的定义，显然是从小区间推导出大区间的过程，所以两层循环的模板如下：

          for (int len=2; len<=N; len++)
            for (int i=0; i<=N-len; i++)
            {
                int j = i+len-1;
                dp[i][j] = 1+dp[i+1][j];

                for (int k=i+1; k<=j; k++)
                {
                    if (s[k]==s[i])
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + ((k+1>j)?0:dp[k+1][j]));
                }
            }
初始条件是：

dp[i][j]==1 when i==j，即len的长度为1;
dp[i][j]==0 when i>j; C语言里如果用int[][]来定义二维数组的话，元素默认值都是0.
"""

"""
Let dp(i, j) be the number of turns needed to print S[i:j+1].

Note that whichever turn creates the final print of S[i], might as well be the first turn, and also there might as well only be one print, since any later prints on interval [i, k] could just be on [i+1, k].

So suppose our first print was on [i, k]. We only need to consider prints where S[i] == S[k], because we could instead take our first turn by printing up to the last printed index where S[k] == S[i] to get the same result.

Then, when trying to complete the printing of interval [i, k] (with S[i] == S[k]), the job will take the same number of turns as painting [i, k-1]. This is because it is always at least as good to print [i, k] first in one turn rather than separately.

Also, we would need to complete [k+1, j]. So in total, our candidate answer is dp(i, k-1) + dp(k+1, j). Of course, when k == i, our candidate is 1 + dp(i+1, j): we paint S[i] in one turn, then paint the rest in dp(i+1, j) turns."""

import functools

class SolutionDFS1:
    def strangePrinter(self, s):
        @functools.lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            res = dfs(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    res = min(res, dfs(i, k - 1) + dfs(k + 1, j))
            return res

        return dfs(0, len(s) - 1)


class SolutionDFS2:
    def strangePrinter(self, s):
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        res = self.dfs(s, i + 1, j, memo) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                res = min(res, self.dfs(s, i, k - 1, memo) + self.dfs(s, k + 1, j, memo))
        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:
    def strangePrinter(self, s):
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if i > j:
            return 0
        res = self.dfs(s, i + 1, j, memo) + 1
        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                res = min(res, self.dfs(s, i, k - 1, memo) + self.dfs(s, k + 1, j, memo))
        return res


class SolutionTony:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if i > j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        res = self.dfs(s, i + 1, j, memo) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                if k + 1 > j:
                    res = min(res, self.dfs(s, i, k - 1, memo))
                else:
                    res = min(res, self.dfs(s, i, k - 1, memo) + self.dfs(s, k + 1, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]




class Solution:
    def strangePrinter(self, s):
        n = len(s)
        dp = [[0] * n for i in range(n + 1)]
        for i in range(n):
            dp[i][i] = 1

        for step in range(1, n):
            for i in range(n-step):
                j = i+step
                dp[i][j] = dp[i+1][j] + 1
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k+1][j])
        return dp[0][-1] if s else 0




class Solution2:
    def strangePrinter(self, s):
        if not s:
            return 0
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for step in range(2, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                dp[i][j] = 1 + dp[i + 1][j]
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        if k + 1 > j:
                            dp[i][j] = min(dp[i][j], dp[i][k - 1])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
        return dp[0][n - 1]



