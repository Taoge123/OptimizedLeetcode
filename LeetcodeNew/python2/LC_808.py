import collections

"""
题目大意：
有A，B两种汤。初始每种汤各有N毫升，现有4种操作：

1. A倒出100ml，B倒出0ml
2. A倒出75ml， B倒出25ml
3. A倒出50ml， B倒出50ml
4. A倒出25ml， B倒出75ml
每种操作的概率均等为0.25。如果汤的剩余容量不足完成某次操作，则有多少倒多少。当每一种汤都倒完时停止操作。

求A先倒完的概率，加上A和B同时倒完的概率。

解题思路：
记忆化搜索 + 特判

if A <= 0 and B <= 0: dp[A][B] = 0.5 

elif A <= 0: dp[A][B] = 1 

elif B <= 0: dp[A][B] = 0

else: dp[A][B] = 0.25 * (dp[A - 100][B] + dp[A - 75][B - 25] + dp[A - 50][B - 50] + dp[A - 25][B - 75])
当N >= 14000时，近似等于1，直接返回1即可
"""

class Solution1:
    def soupServings(self, N):
        self.memo = {}
        if N >= 5500:
            return 1.0
        return self.dfs(N, N)

    def dfs(self, A, B):
        if A <= 0 and B <= 0:
            return 0.5
        if A <= 0:
            return 1
        if B <= 0:
            return 0
        if (A, B) in self.memo:
            return self.memo[(A, B)]
        res = 0.25 * (self.dfs(A - 100, B) + self.dfs(A - 75, B - 25) +
                      self.dfs(A - 50, B - 50) + self.dfs(A - 25, B - 75))
        self.memo[(A, B)] = res
        return res



class Solution:
    def soupServings(self, N: int) -> float:
        if N == 0:
            return 0.5
        if N > 5000:
            return 1
        self.memo = collections.defaultdict(int)
        self.dfs(N, N)
        return self.memo[(N, N)]

    def dfs(self, A, B):
        if B > 0 and A <= 0:
            return 1
        if A <= 0 and B <= 0:
            return 0.5
        if B <= 0 and A > 0:
            return 0
        if (A, B) in self.memo:
            return self.memo[(A, B)]

        res = 0.25 * self.dfs(A - 100, B) + 0.25 * self.dfs(A - 75, B - 25) + 0.25 * self.dfs(A - 50,
                                                                                              B - 50) + 0.25 * self.dfs(
            A - 25, B - 75)
        self.memo[(A, B)] = res
        return res



