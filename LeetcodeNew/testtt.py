class Solution:
    def stoneGameVII(self, stones) -> int:
        memo = {}
        score = self.dfs(stones, 0, len(stones) - 1, memo)
        return score

    def dfs(self, nums, i, j, memo):
        # n = len(nums)
        if i+1 == j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        x = sum(nums[i+1:j]) - self.dfs(nums, i + 1, j, memo)
        y = sum(nums[i:j-1]) - self.dfs(nums, i, j - 1, memo)
        memo[(i, j)] = max(x, y)
        return memo[(i, j)]




stones = [7,90,5,1,100,10,10,2]
a = Solution()
print(a.stoneGameVII(stones))


