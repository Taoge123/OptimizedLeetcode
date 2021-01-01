

"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""



class SolutionDFS1:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0

            res = 0
            for k in range(i + 1, j):
                res = max(res, nums[i] * nums[k] * nums[j] + dfs(i, k) + dfs(k, j))

            return res

        return dfs(0, len(nums) - 1)



class SolutionDFS2:
    def maxCoins(self, nums) -> int:
        memo = {}
        nums = [1] + nums + [1]
        return self.dfs(nums, 0, len(nums) - 1, memo)

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 0

        res = 0
        for k in range(i + 1, j):
            res = max(res, nums[i] * nums[k] * nums[j] + self.dfs(nums, i, k, memo) + self.dfs(nums, k, j, memo))

        memo[(i, j)] = res
        return memo[(i, j)]



class Solution:
    def maxCoins(self, nums) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0 for i in range(n)] for j in range(n)]

        for step in range(2, n):
            for i in range(n - step):
                j = i + step
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][n - 1]





"""
[0, 0, 3, 30, 159, 167]
[0, 0, 0, 15, 135, 159]
[0, 0, 0, 0,  40,  48]
[0, 0, 0, 0,  0,   40]
[0, 0, 0, 0,  0,   0]
[0, 0, 0, 0,  0,   0]

"""




nums = [1,2,3,4,5,6,7]
a = Solution()
print(a.maxCoins(nums))



