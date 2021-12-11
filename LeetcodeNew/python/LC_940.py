"""
https://leetcode.com/problems/distinct-subsequences-ii/discuss/777819/Python-Recursive-Soln-DP

940.Distinct-Subsequences-II
尝试构造状态dp[i]，表示截止第i个字符为止，我们能够创建的distinct子序列有多少．对于第i个字符ch，我们尝试思考它本身是否参与到子序列的构建中来．

情况I:如果它不参与到子序列的构建，那么dp[i-1]有多少子序列，dp[i]一定会保留全部的这些，所以dp[i]+=dp[i-1]

情况II:如果它参与到子序列的构建，那么dp[i-1]有多少子序列,末位加上S[i]之后，似乎就能生成同样多的新的子序列了．所以继续有dp[i]+=dp[i-1]．所以综合一下，dp[i]=dp[i-1]*2?

但是慢着，有一种疏漏的情况．举个例子"aaa"，考虑前两个元素的时候，可以有两种子序列"a","aa"；当考虑第三个元素的时候，不加a和加a这两种方案，会分别产生"a","aa"以及"aa","aaa"这四种方案，
可以发现有重复出现了。归根结底的原因是，在考虑dp[i-1]的时候，有些子序列已经是以a结尾的，比如XXXXa；而当考虑S[i]==a的时候，如果不加这个新元素，
会有之前的XXXXa，而加这个新元素，也会有新的XXXX+a，这些都是重复的，而重复的次数就是这种XXXX的个数。这个XXXX的个数怎么计算呢，那就是找在i之前出现S[j]==S[i]的位置，dp[j-1]就是统计了这样的XXXXa的个数！

所以综上，dp[i]的更新式子是:dp[i] = dp[i-1]*2-dp[j-1)其中j就是[1:i-1]里最后一个满足S[j]==S[i]的index。

另外，以上的dp[i]都包括了空subseuence的情况。最后的结果应该排除这个，即输出的是dp[N]-1.

补充
有一个听众问我，为什么去重的操作里，只需要减去dp[j-1]（j是上一个满足S[j]==S[i]的字符的index），而不减去其他的dp[k-1]（k是在j更早之前的某些字符，也满足S[k]==S[i])。这个问题很深刻。

我举个例子：...XXX... (a1) ...YYY... (a2) ...ZZZ... (a3), 其中a1,a2,a3都代表相同的字符a，他们对应的index分别是k,j,i. XXX/YYY/ZZZ表示在各自区间内取的某个subsequence.

我们在计算dp[i]的时候，减去了dp[j-1]，这是因为这两部分是重复的：

XXXYYY(a2)
XXXYYY(a3)
而我们为什么没有考虑下面这两部分的重复呢？

XXX(a1)
XXX(a3)
这是因为XXX(a1)本质是和XXXYYY(a2)重合的！就最终的subsequence的样子而言，前者就是后者的一部分。我们计算dp[i]时，
减去的dp[j-1]，去掉了形如XXXYYY(a2)的重复，其实也就已经去掉了形如XXX(a1)的重复。所以我们不需要考虑其他在j之前的任何S[k]==S[i]的case。


X X X X X X X X X X X Xi

X
XX
XXX
Xi
XXi
XXXi

It will at least doubled -> dp[i] = dp[i-1] * 2
then we dedupulicate


X X X X X X X S[j]=a X X X X X S[i]=a
找到最靠后的j, s[j] == s[i]
dp[i] = dp[i-1]*2 - dp[j-1]

"""

import functools


class SolutionTD:
    def distinctSubseqII(self, s: str) -> int:
        memo = {}
        mod = 10 ** 9 + 7
        n = len(s)

        def dfs(i):
            if i == n:
                return 1

            val = dfs(i + 1)

            if s[i] not in memo:
                memo[s[i]] = val % mod
                return val * 2
            else:
                res = (val * 2 - memo[s[i]])
                memo[s[i]] = val
                return res % mod

        return dfs(0) - 1



class SolutionMemo:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            visited = set()
            res = 0
            for j in range(i, n):
                if s[j] in visited:
                    continue
                visited.add(s[j])
                res = res + 1 + dfs(j + 1)
                res %= mod

            return res
        return dfs(0)



class SolutionMemo2:
    def distinctSubseqII(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, memo)

    def dfs(self, s, i, memo):
        if i in memo:
            return memo[i]

        mod = 10 ** 9 + 7
        n = len(s)
        if i == n:
            return 0

        visited = set()
        res = 0
        for j in range(i, n):
            if s[j] in visited:
                continue
            visited.add(s[j])
            res = res + self.dfs(s, j + 1, memo) + 1
            res %= mod

        memo[i] = res
        return res



class Solution:
    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        table = {}
        mod = 10 ** 9 + 7

        for i in range(1, n+1):
            dp[i] = (dp[i - 1] * 2) % mod
            if S[i - 1] in table:
                dp[i] = (dp[i] - dp[table[S[i - 1]] - 1]) % mod
            table[S[i - 1]] = i

        return dp[n] - 1


s = "aaa"
a = SolutionMemo2()
print(a.distinctSubseqII(s))

