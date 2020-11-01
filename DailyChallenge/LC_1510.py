
import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        # base case not necessary
        # if n == 0:
        #     return False

        for i in range(1, int(math.sqrt(n) ) +1):
            if self.dfs(n - i* i, memo) == False:
                memo[n] = True
                return True

        memo[n] = False
        return False



