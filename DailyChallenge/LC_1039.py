
class Solution:
    def minScoreTriangulation(self, A) -> int:
        memo = {}
        return self.dfs(A, 0, len(A ) -1, memo)

    def dfs(self, nums, i, j, memo):
        # if i >= j:
        #     return 0
        if j- i + 1 < 3:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        res = float("Inf")
        for k in range(i + 1, j):
            res = min(res, nums[i] * nums[k] * nums[j] + self.dfs(nums, i, k, memo) + self.dfs(nums, k, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]





