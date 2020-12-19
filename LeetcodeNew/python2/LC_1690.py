class Solution:
    def stoneGameVII(self, stones) -> int:
        presum = [0]
        for num in stones:
            presum.append(num + presum[-1])

        n = len(stones)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        return self.dfs(stones, presum, 0, len(stones) - 1, memo)

    def dfs(self, stones, presum, i, j, memo):
        if i > j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        a = presum[j + 1] - presum[i + 1] - self.dfs(stones, presum, i + 1, j, memo)
        b = presum[j] - presum[i] - self.dfs(stones, presum, i, j - 1, memo)

        memo[i][j] = max(a, b)
        return max(a, b)



class Solution2:
    def stoneGameVII(self, stones) -> int:
        presum = [0]
        for num in stones:
            presum.append(num + presum[-1])

        n = len(stones)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        # memo = {}
        # @functools.lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            a = presum[j + 1] - presum[i + 1] - dfs(i + 1, j)
            b = presum[j] - presum[i] - dfs(i, j - 1)

            memo[i][j] = max(a, b)
            return max(a, b)

        return dfs(0, len(stones) - 1)




