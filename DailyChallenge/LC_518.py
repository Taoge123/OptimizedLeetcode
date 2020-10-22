class Solution:
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



class Solution2:
    def change(self, amount: int, coins) -> int:
        if not coins:
            retu

        memo = {}
        return self.dfs(amount, tuple(coins), memo, 0)

    def dfs(self, amount, coins, memo, pos):
        if pos == len(coins):
            return 0

        if amount == 0:
            return 1

        if amount < 0 or len(coins) == 0:
            return 0

        if (amount, pos) in memo:
            return memo[(amount, pos)]
        # we can either pick or not to pick pos coin, if we pick it, then pos stay the saame since we are allow to pick it again
        # if we do not pick the pos coin, then pos move forward with amount dont chsnge
        res = self.dfs(amount - coins[pos], coins, memo, pos) + self.dfs(amount, coins, memo, pos + 1)
        memo[amount, pos] = res
        return memo[amount, pos]

