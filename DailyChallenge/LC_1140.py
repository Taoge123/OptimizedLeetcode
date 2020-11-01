
class Solution:
    def stoneGameII(self, piles) -> int:
        memo = {}
        return self.dfs(0, 1, piles, memo)

    def dfs(self, i, M, piles, memo):
        n = len(piles)
        if (i, M) in memo:
            return memo[(i, M)]

        if i >= n:
            return 0

        if i+ 2 * M >= n:
            return sum(piles[i:])

        res = 0
        for x in range(1, 2 * M + 1):
            newM = max(M, x)
            res = max(res, sum(piles[i:]) - self.dfs(i + x, newM, piles, memo))
            memo[(i, M)] = res

        return memo[(i, M)]


