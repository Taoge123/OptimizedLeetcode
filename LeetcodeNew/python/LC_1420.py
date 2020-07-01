"""

https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/solution/dong-tai-gui-hua-by-nks5117/

dp[i][j][k] : the number of ways to build the array[1:i] and max(arr[1:i])=j and search cost is k

if arr[i] is the largest among arr[1:i] => arr[i] = j, 那么前i-1个元素最大值可以是1,...,j-1任意一个
dp[i][j][k] += sum(dp[i-1][1..j-1][k-1]), 最大值是j， 前面的可以是任何小于j的数, 就有j中可能性


if arr[i] is not the largest among arr[1:i] => arr[i] <= j
dp[i][j][k] += dp[i-1][1..j-1][k-1] * j


----------------------------------------------------------------------------------------------------------------------------
dp[i][j][k] : the number of ways to build the array[1:i] and max(arr[1:i])-j and search cost is k


if arr[i] is the largest among arr[1:i] => arr[i] = j
dp[i][j][k] += sum(dp[i-1][1..j-1][k-1])

if arr[i] is not the largest among arr[1:i] => arr[i] <= j
dp[i][j][k] += dp[i-1][1..j-1][k-1]


1420.Build-Array-Where-You-Can-Find-The-Maximum-Exactly-K-Comparisons
乍看没有头绪，不妨将题目中的三个变量都作为dp状态变量的下标试一下。第一版本是：dp[i][j][k]表示对于前i个元素、当nums[i]等于j、总共用了k次cost时，总共有多少种方案。

我们试图来转移dp[i][j][k]到前一个状态dp[i-1][?][?]。考虑假设我们在处理第i个元素的时候动用了一次cost，那么意味着前i-1个元素必须都小于j。但是我们的dp设计里并没有这样的信息。
dp[i-1][j'][k-1]中的j'表示的仅仅是nums[i]==j'，没有合适的状态来表示前i-1个元素的最大值。

所以我们容易想到并改进得到第二个版本：dp[i][j][k]表示对于前i个元素、最大值等于j、总共用了k次cost时，总共有多少种方案。

同样，考虑假设我们在处理第i个元素的时候新增一次cost，那么意味着nums[i]就是前i个元素的最大值，即是j。于是我们需要前i-1个元素的最大值小于j就可以了。
因此有dp[i][j][k] = dp[i-1][j'][k-1]，其中j'=1,2,...,j-1.

考虑假设我们在处理第i个元素的时候没有新增一次cost，那么意味着nums[i]并不是前i个元素的最大值，因此nums[i]的取值可以是1,2,..j.
而对于前i-1个元素的最大值则必须是j。因此有dp[i][j][k] = dp[i-1][j][k]*j.

这里根据加法原理，dp[i][j][k]应该是上面两种情况之和。

最后的答案是dp[n-1][j][k], j=1,2,..m 的总和。

"""


class SolutionWisdom:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        K = k
        dp = [[[0 for i in range(K + 1)] for j in range(m + 1)] for k in range(n)]
        mod = 10 ** 9 + 7

        for j in range(1, m + 1):
            dp[0][j][1] = 1

        for i in range(1, n):
            for j in range(1, m + 1):
                for k in range(1, K + 1):
                    for t in range(1, j):
                        dp[i][j][k] += dp[i - 1][t][k - 1]
                        dp[i][j][k] %= mod
                    dp[i][j][k] += dp[i - 1][j][k] * j
                    dp[i][j][k] %= mod

        res = sum([dp[n - 1][j][k] for j in range(1, m + 1)])
        res %= mod
        return res





"""
Explanation

In this question, searchcost is basically the number of times when the largest number in array increased.

It's obvious that we should use dynamic programming to approach this problem. Let's define dp(arr_len, lrg_num, search_cost) as follows:

arr_len: the length of current array
lrg_num: the largest number in current array
search_cost: the searchcost of current array
And dp(arr_len, lrg_num, search_cost) means the number of arrays with current length arr_len, largest number lrg_num, 
and the largest number increased by search_cost times so far.

Suppose we are building an array from left to right. The transition function has two cases: the last number contributes to searchcost vs not.

Let's take array [num, 5] as an example. We loop through 1 to m for num.

num = 5, ..., m: No searchcost happens on last number. The largest number is unchanged from [num] to [num, 5].
num = 1, ..., 4: Searchcost happens on last number.
And we have the following transition function:

dp(arr_len, lrg_num, search_cost) += dp(arr_len - 1, lrg_num, search_cost) for num = lrg_num + 1, ..., m
dp(arr_len, lrg_num, search_cost) += dp(arr_len - 1, num, search_cost - 1) for num = 1, ..., lrg_num
"""

from functools import lru_cache

class SolutionAlan:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        @lru_cache(None)
        def dp(arr_len, lrg_num, search_cost):
            if arr_len == 1:
                return 1 if search_cost == 1 else 0
            if search_cost == 0:  # optional
                return 0

            # no searchcost happens on last number
            res = dp(arr_len - 1, lrg_num, search_cost) * lrg_num

            # searchcost happens on last number
            res += sum(dp(arr_len - 1, num, search_cost - 1) for num in range(1, lrg_num))

            return res % 1000000007

        return sum([dp(n, num, k) for num in range(1, m + 1)]) % 1000000007





class Solution2:
    def dfs(self, n, i, k):
        if (self.tmp[n][i][k] != -1):
            return self.tmp[n][i][k]
        if n == 0 or k == 0 or i == 0:
            self.tmp[n][i][k] = 0
            return 0
        if n == 1 and k == 1:
            self.tmp[n][i][k] = 1
            return 1
        res = 0
        for j in range(1, i):
            res += self.dfs(n - 1, j, k - 1)
            res %= 1000000007
        res += self.dfs(n - 1, i, k) * i
        res %= 1000000007
        self.tmp[n][i][k] = res
        return res

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.tmp = [[[-1 for t in range(k + 1)] for j in range(m + 1)] for i in range(n + 1)]
        res = 0
        for i in range(1, m + 1):
            res += self.dfs(n, i, k)
            res %= 1000000007
        return res







