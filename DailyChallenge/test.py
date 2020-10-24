#
# class Solution:
#     def coinChange(self, coins, amount: int) -> int:
#         memo = {0 : 0}
#         coins.sort()
#
#         res =  self.dfs(coins, amount, memo)
#         if res != float('inf'):
#             return res
#         return -1
#
#
#     def dfs(self, coins, amount, memo):
#         if amount in memo:
#             return memo[amount]
#
#         res = float('inf')
#
#         for coin in coins:
#             if amount - coin >= 0:
#                 res = min(res, self.dfs(coins, amount - coin, memo) + 1)
#
#         memo[amount] = res
#         return memo[amount]


class Solution:
    def change(self, amount: int, coins) -> int:
        memo = {0: 1}
        test = []
        coins.sort()
        a = self.dfs(coins, amount, [], test, memo, 0)
        print(test)
        return a

    def dfs(self, coins, amount, path, test, memo, pos):
        print(pos)
        if amount == 0:
            test.append(path)
            return 1
        if amount < 0:
            return 0

        res = 0
        for coin in coins[pos:]:
            if amount < coin:
                break
            res += self.dfs(coins, amount - coin, path + [coin], test, memo, pos)
        memo[amount] = res
        return memo[amount]


amount = 5
coins = [1,2,5]
a = Solution()
print(a.change(amount, coins))



