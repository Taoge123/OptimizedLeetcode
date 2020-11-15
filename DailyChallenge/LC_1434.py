
class SolutionDFS:
    def numberWays(self, hats) -> int:
        memo = {}
        return self.dfs(hats, 0, 0, memo)

    def dfs(self, hats, cur, state, memo):
        n = len(hats)
        N = (1 << n) - 1
        mod = 10 ** 9 + 7

        if (cur, state) in memo:
            return memo[(cur, state)]

        if state == (1 << n) - 1:
            return 1

        if cur > 40:
            return 0

        res = self.dfs(hats, cur + 1, state, memo)

        for i in range(n):
            if cur in hats[i] and state & (1 << i) == 0:
                res += self.dfs(hats, cur + 1, state + (1 << i), memo)

        memo[(cur, state)] = res
        return res % mod


