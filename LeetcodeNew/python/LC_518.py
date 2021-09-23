
"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

import functools


class SolutionTony:
    def change(self, amount: int, coins) -> int:

        @functools.lru_cache(None)
        def dfs(amount, i):
            if amount == 0:
                return 1

            if amount < 0 or i >= len(coins):
                return 0

            take = dfs(amount - coins[i], i)
            no_take = dfs(amount, i + 1)

            return take + no_take

        return dfs(amount, 0)


class SolutionTonnie:
    def change(self, amount: int, coins) -> int:

        memo = {}
        return self.dfs(coins, 0, amount, memo)

    def dfs(self, nums, i, target, memo):
        if (i, target) in memo:
            return memo[(i, target)]

        n = len(nums)
        if target == 0:
            return 1
        if target < 0 or i >= n:
            return 0

        take = self.dfs(nums, i, target - nums[i], memo)
        no_take = self.dfs(nums, i + 1, target, memo)

        memo[(i, target)] = take + no_take
        return memo[(i, target)]


class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(1, amount + 1):
                if j >= coin:
                    dp[j] += dp[j - coin]

        return dp[amount]



class SolutionTLE:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 1

        if amount < 0 or len(coins) == 0:
            return 0

        return self.change(amount - coins[0], coins) + self.change(amount, coins[1:])


class Solutioncache:
    def change(self, amount: int, coins) -> int:

        @functools.lru_cache(None)
        def dfs(amount, coins):
            if amount == 0:
                return 1

            if amount < 0 or len(coins) == 0:
                return 0

            return dfs(amount - coins[0], coins) + dfs(amount, coins[1:])

        return dfs(amount, tuple(coins))


class SolutionCache2Slow:
    def change(self, amount: int, coins) -> int:
        return self.dfs(amount, tuple(coins))

    @functools.lru_cache(None)
    def dfs(self, amount, coins):
        if amount == 0:
            return 1

        if amount < 0 or len(coins) == 0:
            return 0

        return self.dfs(amount - coins[0], coins) + self.dfs(amount, coins[1:])



class Solution3:
    def change(self, amount: int, coins) -> int:
        if not coins:
            if amount == 0:
                return 1
            return 0

        coins.sort()
        return self.dfs(amount, coins, 0, {})

    def dfs(self, amount, coins, idx, memo):
        if (amount, idx) in memo:
            return memo[(amount, idx)]

        if amount == 0:
            return 1

        res = 0
        for i in range(idx, len(coins)):
            if amount - coins[i] < 0:
                break
            res += self.dfs(amount - coins[i], coins, i, memo)

        memo[(amount, idx)] = res
        return res




amount = 5
coins = [1, 2, 5]
a = Solution()
print(a.change(amount, coins))



"""
[1, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 0, 0]
[1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
[1, 1, 2, 1, 1, 1]
[1, 1, 2, 2, 1, 1]
[1, 1, 2, 2, 3, 1]
[1, 1, 2, 2, 3, 3]
[1, 1, 2, 2, 3, 3]
[1, 1, 2, 2, 3, 3]
[1, 1, 2, 2, 3, 3]
[1, 1, 2, 2, 3, 3]
"""




