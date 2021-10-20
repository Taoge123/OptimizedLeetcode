
"""

1575.Count-All-Possible-Routes
解法1：o(f*n*n)
当我们考虑到达城市c有多少种方案的时候，势必会考虑之前可能在哪个城市？如果之前的城市是d，那么问题就转化为了“达到城市d多少种方案”，另外加上一个约束：有足够的剩余油量能够从d来到c。所以每到一个城市的剩余油量亦是一个关键因素。

本题最大的提示就是fuel的数据范围只有200，因此我们暴力遍历这个变量空间的所有值都是可行的。什么意思？就是我们可以定义状态dp[f][c]表示（从初始状态）到达城市c、剩余油料是f时，有多少种行程方案。因此我们可以根据上面的思路，遍历c之前的一站d。令d和c之间的油料消耗是g，那么说明前一站的状态就是dp[f+g][d]。如果知道有多少方案能够达到dp[f+g][d]，那么就说明有相同数量的方案可以达到dp[f][c]。所以状态转移方程是：

for (int d=0; d<n; d++)
  g = dis(c,d);
  dp[f][c] += dp[f+g][d];
此外要注意d不能与c重复，此外f+g不能超过初始油量fuel.

最终的答案是sum {dp[f][finish]}，其中油量f可以是任意值。因为不同的方案，达到终点的油量都不一样。我们需要把每种方案都累加起来。

解法2：o(f*n)
上面的解法中，我们考虑dp[f][c]之前的状态，会遍历其他的任意一个城市d。但是不管是哪一个城市d，想要到达城市c的时候，都会经过c的左邻城市和c的右邻城市。我们其实只需要观察到达（或者经过）c的左邻/右邻城市有多少走法就行。

举个例子：令城市编号0,1,2,3代表着实际位置。start在城市0，finish在城市3.初始油料就是3.那么我们有三种方案：

0-1-2-3
0-1-3
0-2-3
0-3
所以我们考虑从左边抵达dp[f][3]的那些方法，需要考察dp[f+3][0],dp[f+2][1],dp[f+1][2].但是这三种情况，其实有一个共性：即当油量为f+1的时候位于城市2.那么我们是否可以把这三种状态都归纳为一种，这样dp[f][3]的状态只需要从dp[f+1][2]转移过去呢？当然是不可以的。因为我们要区分“停留”和“路过”。根据我们的dp定义，dp[f][c]表示的是当存留油量为f时，停留在c的方法。任何仅是路过c的方案，都不能统计在最终到达c的方案里。

这就提示我们设计这样的dp[f][c][k]，第三维k=0表示停留，k=1表示向左路过，k=2表示向右路过。状态转移方程是：

        for (int f=fuel; f>=0; f--)
            for (int c=0; c<n; c++)
            {
                if (c>0 && f+locations[c]-locations[c-1] <= fuel)
                {
                    int gas = locations[c]-locations[c-1];
                    dp[f][c][0] += dp[f+gas][c-1][0] + dp[f+gas][c-1][2];
                    dp[f][c][2] += dp[f+gas][c-1][0] + dp[f+gas][c-1][2];
                }
                if (c<n-1 && f+locations[c+1]-locations[c] <= fuel)
                {
                    int gas = locations[c+1]-locations[c];
                    dp[f][c][0] += dp[f+gas][c+1][0] + dp[f+gas][c+1][1];
                    dp[f][c][1] += dp[f+gas][c+1][0] + dp[f+gas][c+1][1];
                }
                dp[f][c][0]%=M;
                dp[f][c][1]%=M;
                dp[f][c][2]%=M;
            }
从dp[f][c][0] += dp[f+gas][c-1][0] + dp[f+gas][c-1][2]这一行可以看出，对于所有从左边城市达到c的方案，不必列举前一站的城市，因为他们都会“路过”第c-1个城市。我们只需要再额外考虑“停留”在c-1这座城市的方案。

最终的答案是sum{dp[f][finish][0]} for all f，但是注意因为locations需要排序，此时的finish的编号和之前的并不一致，需要额外处理一下。


dp[f][c]: when arriving at city c, with fuel f left

for d in range(n):
    gas = abs(locations[d] - locations[c])
    dp[f][c] += dp[f+gas][d]

return sum(dp[f][finish]) for all f

"""

"""
dp[f][c]: when arriving at city c, with fuel f left

for d in range(n):
    gas = abs(locations[d] - locations[c])
    dp[f][c] += dp[f+gas][d]

return sum(dp[f][finish]) for all f


dp[f][3] <- dp[f+1][2], dp[f+2][1], dp[f+3][0]


0 1 2 3

dp[f][c][k] k=0: stay, k=1: moving right, k=2: moving left

for f in range(fuel, -1, -1):
    for c in range(n):
        if c>0:
            gas = lications[c] - locations[c-1]
            dp[f][c][0] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
            dp[f][c][1] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
        if c < n-1:
            gas = lications[c+1] - locations[c-1]
            dp[f][c][0] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]
            dp[f][c][2] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]

return sum{dp[f][finish][0]} for all f

"""

import functools


class Solution:
    def countRoutes(self, nums, start: int, finish: int, fuel: int) -> int:

        n = len(nums)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(node, k):
            if k < 0:
                return 0

            res = 0
            if node == finish:
                res += 1

            for nei in range(n):
                if nei == node:
                    continue
                res += dfs(nei, k - abs(nums[nei] - nums[node]))

            return res % mod

        return dfs(start, fuel)



class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        dp = [[[0 for i in range(3)] for j in range(201)] for _ in range(201)]
        mod = 10 ** 9 + 7
        startPos = locations[start]
        finishPos = locations[finish]
        locations.sort()
        n = len(locations)

        startIdx, finishIdx = 0, 0
        for i in range(n):
            if locations[i] == startPos:
                startIdx = i
            if locations[i] == finishPos:
                finishIdx = i

        dp[fuel][startIdx][0] = 1

        for f in range(fuel, -1, -1):
            for c in range(n):
                if c > 0 and f + locations[c] - locations[c - 1] <= fuel:
                    gas = locations[c] - locations[c - 1]
                    dp[f][c][0] += dp[f + gas][c - 1][1] + dp[f + gas][c - 1][0]
                    dp[f][c][1] += dp[f + gas][c - 1][1] + dp[f + gas][c - 1][0]
                if c < n - 1 and f + locations[c + 1] - locations[c] <= fuel:
                    gas = locations[c + 1] - locations[c]
                    dp[f][c][0] += dp[f + gas][c + 1][2] + dp[f + gas][c + 1][0]
                    dp[f][c][2] += dp[f + gas][c + 1][2] + dp[f + gas][c + 1][0]

        dp[f][c][0] %= mod
        dp[f][c][1] %= mod
        dp[f][c][2] %= mod

        res = 0
        for f in range(fuel + 1):
            res = (res + dp[f][finishIdx][0]) % mod
        return res




class SolutionTLE:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        dp = [[0 for i in range(101)] for j in range(201)]
        mod = 10 ** 9 + 7
        n = len(locations)
        dp[fuel][start] = 1

        for f in range(fuel, -1, -1):
            for c in range(n):
                for d in range(n):
                    if d == c:
                        continue
                    gas = abs(locations[d] - locations[c])
                    if f + gas <= fuel:
                        dp[f][c] = (dp[f][c] + dp[f + gas][d]) % mod

        res = 0
        for f in range(fuel + 1):
            res = (res + dp[f][finish]) % mod
        return res





