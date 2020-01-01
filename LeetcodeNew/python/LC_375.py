
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = [[0] * (n+1) for i in range(n+1)]
        return self.helper(1, n, cache)

    def helper(self, i, j, cache):
        if i >= j:
            return 0
        if cache[i][j] != 0:
            return cache[i][j]
        res = float('inf')
        for num in range(i, j+1):
            res = min(res, max(self.helper(i, num-1, cache), self.helper(num+1, j, cache)) + num)
        cache[i][j] = res
        return res


class Solution2:
    def getMoneyAmount(self, n: int) -> int:

        cache = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for lo in range(n - 1, 0, -1):
            for hi in range(lo + 1, n + 1):
                cache[lo][hi] = float('inf')
                for num in range(lo, hi):
                    cache[lo][hi] = min(cache[lo][hi], num + max(cache[lo][num - 1], cache[num + 1][hi]))

        return cache[1][n]



n = 4
a = Solution2()
print(a.getMoneyAmount(n))




