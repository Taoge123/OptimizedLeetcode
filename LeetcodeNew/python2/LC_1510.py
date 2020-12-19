"""
n: n-1, n-4, n-9, ... ,


"""

import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.memo = {}
        for i in range(1, n + 1):
            self.memo[i] = -1
        return self.dfs(n)

    def dfs(self, n):
        if n in self.memo and self.memo[n] != -1:
            return self.memo[n]

        for i in range(1, int(math.sqrt(n)) + 1):
            if self.dfs(n - i * i) == False:
                self.memo[n] = 1
                return True

        self.memo[n] = 0
        return False




