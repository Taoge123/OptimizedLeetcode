
"""
https://www.youtube.com/watch?v=uzfsrChj8dM
https://leetcode.com/problems/stone-game-iii/discuss/564342/JavaC%2B%2BPython-Dynamic-Programming
https://medium.com/algorithm-solving/leetcode-1406-stone-game-iii-e575add6530b
https://blog.csdn.net/qq_17550379/article/details/105402637


Solution 1: DP
dp[i] means, if we ignore before A[i],
what's the highest score that Alex can win over the Bob？

There are three option for Alice to choose.
Take A[i], win take - dp[i+1]
Take A[i] + A[i+1], win take - dp[i+2]
Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]
dp[i] equals the best outcome of these three solutions.


Complexity
Time O(N^)
Space O(N)

"""


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

