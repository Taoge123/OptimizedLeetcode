
"""
https://leetcode.com/problems/coin-change/solution/
https://www.youtube.com/watch?v=jgiZlGzXMBw
https://blog.csdn.net/fuxuemingzhu/article/details/83592442
http://bookshadow.com/weblog/2015/12/27/leetcode-coin-change/



You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

"""
This solution is inspired by the BFS solution for problem Perfect Square. 
Since it is to find the least coin solution (like a shortest path from 0 to amount), 
using BFS gives results much faster than DP.
"""
class SolutionBFS1:
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1


"""
Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, 

dp[i] = min(dp[i - coin] + 1).

The time complexity is O(amount * coins.length) and the space complexity is O(amount)
"""
"""
思路： 
本题意思是有一堆不同面额的硬币，问最少取多少枚硬币，可以凑够想要的面值，每种硬币数无限。

假设dp[i]表示凑够i元所需要的最少硬币数，一共有n种面值硬币，
那么dp[i]=min(dp[i−coins[0]],dp[i−coins[1]],...dp[i−coins[k])+1，其中coins[k]<=idp[i]=min(dp[i−coins[0]],dp[i−coins[1]],...dp[i−coins[k])+1，

其中coins[k]<=i

比如例1中

dp[0] = 0
dp[1] = 1
dp[2] = min{dp[2-1]}+1
dp[3] = min{dp[3-1],dp[3-2]}+1
dp[4] = min{dp[4-1],dp[4-2]}+1
...
dp[11] = min{11-1},dp[11-2],dp[11-5]}+1
"""

class Solution0:
    def coinChange(self, coins, amount):

        n = len(coins)
        # dp[i]表示amount=i需要的最少coin数
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in range(n):
                # 只有当硬币面额不大于要求面额数时，才能取该硬币
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        # 硬币数不会超过要求总面额数，如果超过，说明没有方案可凑到目标值
        return dp[amount] if dp[amount] <= amount else -1

class Solution1:
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

class Solution2:
    def coinChange(self, coins, amount):

        res = [amount+1] * (amount+1)
        res[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    res[i] = min(res[i], res[i-c] + 1)

        if res[amount] == amount+1:
            return -1
        return res[amount]


class Solution3:
    def coinChange(self, coins, amount):
        dp = [0] * (amount + 1)
        MAX = float("inf")

        # Number of coins needed for coin amount is 1
        # Make sure to exclude sums larger than amount. No need of it
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            # Don't calculate if its a coin that already exists
            if i in coins: continue
            # 1 + min(dp[current value - current coin])
            # The 1 is because we are using current coin
            dp[i] = 1 + min(dp[i - coin] if i - coin >= 0 else MAX for coin in coins)

        return -1 if dp[-1] == MAX else dp[-1]

"""
Classic case of dynamic programing and counter example of greedy.
dp[i] records the minimal coins needed to make up amount i. And it's one more coin than the minimum of dp[i-j] for j in coins.
All value in dp array are initialized as None. If all possibile dp[i-j] are None, 
amount i is not reachable by any combination of coins as we leave it as None as well. 
And I set a None value as -1 since we are required to return -1 if i is not able to be made up of.
"""
"""
解题方法
动态规划
题目比较重要的是硬币无限数量。我们的做法是使用动态规划，需要构建一个长度是amount + 1的dp数组，
其含义是能够成面额从0到amount + 1需要使用的最少硬币数量。

所以我们对每一种面额的硬币，都去计算并更新新添了这种面额的情况下，构成的所有面额需要的最少硬币数量。注意，变量是不同面额的硬币。
dp更新的策略是从coin面额到amount+1的面额依次向后查找，看这个位置能不能用更少的硬币组成（即使用面额是i - coin的需要硬币数量+1).
"""
class Solution4:
    def coinChange(self, coins, amount):

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]


"""
题意：

零钱兑换，让你用最少的零钱数换取目标的数量。如有零钱1,2,5，换成11最少的为5+5+1 ，3个硬币

思路：

dp，设dp[i] 为兑换目标i最少的硬币数。

则有：dp[i + coins[j] ] = min(dp[i + coins[j] ] , dp[i] + 1）

或者 dp[i] = min(dp[i – coins[j]] + 1,dp[i])

说白了就是用当前的硬币能组合成啥，取最小。

第一个A此题=v= 水啊~
"""
"""
思路
动态规划：

假设amount为10，硬币面额为[1,2,5,10],用dp[i]来表示金额i所需要的最少硬币数,那么显然dp[0]=0,因为金额0不需要任何硬币。
此时如果我们取了个硬币5，显然dp[10]=dp[10-5]+1=dp[5]+1，那么此时dp[5]+1是最小值吗？
不一定，因为如果取一枚金额为10的硬币就足够了，此时dp[10]=dp[10-10]+1=0+1=1.所以我们需要在取me某一枚硬币之后，需要更新当前dp[i]的值。
dp[i]=min(dp[i],dp[i-coin]+1)
另外我们需要初始化dp,假设每一个硬币的面额都大于amount，此时我们是找不出硬币组合的，那么dp[amount]=-1，
显然我们不能初始化所有值为-1（负数小于任何正数），我们应该初始化一个“最大值”,比如inf或者amount+1,当遍历所有金额之后，
最后dp[amount]仍然为'最大值'，说明这笔钱不能由任何硬币组合成，那么我们返回-1。取amount+1是因为：假设所有硬币金额都为1，
那么dp[amount]的最大值都为amount，都会小于amount+1
"""
class Solution11:
    def coinChange(self, coins, amount):
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(amount-coin, -1, -1):
                if(dp[i] != float('inf')):
                    for k in range(1, amount + 1):
                        if k*coin + i <= amount:
                            dp[i+k*coin] = min(dp[i+k*coin], dp[i]+k)
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1



class Solution22:
    def coinChange(self, coins, amount):
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] >= amount + 1:
            return -1
        else:
            return dp[amount]


"""
3. dfs
第三种办法，dfs加强剪枝。首先把coins从大到小排列，先使用大的。如果剩余amount正好整除币值，就是一个合法解。
"""
class Solution33:
    def coinChange(self, coins, amount):
        coins = sorted(coins)[::-1]
        self.ans = float('inf')
        def dfs(coins, s, amount, count):
            coin = coins[s]
            # reach last coin
            if s == len(coins) - 1:
                if amount % coin == 0:
                    self.ans = min(self.ans, count + amount / coin)
            else:
                for k in range(amount/coin, -1, -1):
                    if count + k < self.ans:
                        # pruning, only search if new ans is less than current ans
                        dfs(coins, s + 1, amount - k*coin, count+k)           
        dfs(coins, 0, amount, 0)
        if self.ans < float('inf'):
            return self.ans
        else:
            return -1




