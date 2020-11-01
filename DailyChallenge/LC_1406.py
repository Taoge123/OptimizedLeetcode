
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        memo = {}
        score = self.dfs(0, stoneValue, memo)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def dfs(self, i, nums, memo):
        n = len(nums)
        if i in memo:
            return memo[i]

        if i >= n:
            return 0

        res = float('-inf')
        presum = 0
        for x in range(1, 4):
            if i + x - 1 >= n:
                break
            presum += nums[i + x - 1]
            res = max(res, presum - self.dfs(i + x, nums, memo))
        memo[i] = res
        return memo[i]



