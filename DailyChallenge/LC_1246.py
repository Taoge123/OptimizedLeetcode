class Solution:
    def minimumMoves(self, arr) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        res = 1 + self.dfs(arr, i + 1, j, memo)

        for k in range(i + 1, j + 1):
            if arr[i] == arr[k]:
                res = min(res, max(1, self.dfs(arr, i + 1, k - 1, memo)) + self.dfs(arr, k + 1, j, memo))
        memo[(i, j)] = res
        return memo[(i, j)]



