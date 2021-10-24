
"""
https://www.youtube.com/watch?v=3M8q-wB2tmw
A = [1,15,7,9, 2,5,10]
        i
K = 3

dp[i] = dp[j] + max(dp[j:i]) * (i-j) for j = i-1, i, i-K+1


1043.Partition-Array-for-Maximum-Sum
这是一个基本款的DP。我们考虑当前正在处理的最后一个元素A[i]，必然会想到它归为哪个subarray？因为A[i]只可能归为最后一个subarray，
我们自然会联想到这最后一个subarray的长度可能是1,2,...,直至K。于是我们显然会挨个尝试一遍。只要确定最后一个subarray的范围（比如说从j到i，
那么最后一个subarray的sum就能轻易知道（就是这个subarray中的最大值乘以元素个数i-j+1），并且这个subarray前面的所有元素之和恰好就是dp[j-1].

所以状态转移方程就是：

dp[i] = max{ dp[j-1], Max_element over A[j,..i] * (i-j+1)},   for j=i, i-1, ... , i-K+1
另外需要注意一下，j不可能小于0。


"""

import functools


class SolutionTony:
    def maxSumAfterPartitioning(self, A, k):

        n = len(A)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            maxi, res = 0, 0
            for j in range(i, min(n, i + k)):
                maxi = max(maxi, A[j])
                res = max(res, (j - i + 1) * maxi + dfs(j + 1))
            return res

        return dfs(0)



class SolutionTony1:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            # The dfs finds the max result of the range [i, j)
            if j - i <= K:
                return (j - i) * max(A[i:j])

            res = 0
            for k in range(i + 1, i + 1 + K):
                res = max(res, dfs(i, k) + dfs(k, j))
            return res

        return dfs(0, len(A))



class Solution:
    def maxSumAfterPartitioning(self, A, K) -> int:
        n = len(A)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maxi = float('-inf')
            for k in range(1, min(i, K) + 1):
                maxi = max(maxi, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + maxi * k)

        return dp[n]




