
class Solution:
    def stoneGame(self, piles) -> bool:
        self.memo = {}
        return self.dfs(piles, 0, len(piles) - 1) > 0

    def dfs(self, piles, i, j):
        # base case
        if i == j:
            return piles[i]

        # dfs with memo
        if (i, j) not in self.memo:
            take_i = piles[i] - self.dfs(piles, i + 1, j)
            take_j = piles[j] - self.dfs(piles, i, j - 1)
            self.memo[(i, j)] = max(take_i, take_j)

        return self.memo[(i, j)]


class Solution2:
    def stoneGame(self, piles) -> bool:
        memo = {}
        return self.dfs(piles, 0, len(piles)-1, memo) >= 0


    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0

        if i == j:
            return nums[i]

        if not nums:
            return 0

        res = max(nums[i] - self.dfs(nums, i+1, j, memo), nums[j] - self.dfs(nums, i, j-1, memo))
        memo[(i, j)] = res
        return res





class Solution3:
   def stoneGame(self, p):
       n = len(p)
       dp = p[:]
       for step in range(1, n):
           for i in range(n - d):
               j = i + step
               dp[i] = max(p[i] - dp[i + 1], p[j] - dp[i])
       print(dp)
       return dp[0] > 0



p = [5,3,4,5]
a = Solution()
print(a.stoneGame(p))




