"""
n: n-1, n-4, n-9, ... ,


"""

import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.cache = {}
        for i in range(1, n + 1):
            self.cache[i] = -1
        return self.solve(n)

    def solve(self, n):

        if n in self.cache and self.cache[n] != -1:
            return self.cache[n]

        for i in range(1, int(math.sqrt(n)) + 1):
            if self.solve(n - i * i) == False:
                self.cache[n] = 1
                return True

        self.cache[n] = 0
        return False



