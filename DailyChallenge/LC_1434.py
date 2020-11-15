
class SolutionDFS:
    def numberWays(self, hats) -> int:
        memo = {}
        return self.dfs(hats, 0, 0, memo)

    def dfs(self, hats, pos, state, memo):
        n = len(hats)
        N = (1 << n) - 1
        mod = 10 ** 9 + 7

        if (pos, state) in memo:
            return memo[(pos, state)]

        if state == N:
            return 1

        if pos > 40:
            return 0

        res = self.dfs(hats, pos + 1, state, memo)

        for i in range(n):
            if pos in hats[i] and state & (1 << i) == 0:
                res += self.dfs(hats, pos + 1, state + (1 << i), memo)

        memo[(pos, state)] = res
        return res % mod


