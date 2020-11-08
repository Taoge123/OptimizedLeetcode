class Solution:
    def mctFromLeafValues(self, arr) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 0

        res = float('inf')
        for k in range(i, j):
            rootVal = max(arr[i:k + 1]) * max(arr[k + 1:j + 1])
            res = min(res, rootVal + self.dfs(arr, i, k, memo) + self.dfs(arr, k + 1, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]



