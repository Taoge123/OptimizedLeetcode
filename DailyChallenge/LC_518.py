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



