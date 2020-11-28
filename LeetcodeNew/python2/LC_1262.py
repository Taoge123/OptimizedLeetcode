"""
a, b, c
   x  y

x = b
x = b-1
x = b-2

y = c
y = c-1
y = c-2

(1*x+2*y) % 3 == 0


dp[i] : the maximum possible sum (%3==remainder) in the first i elements
X X X X X i
1. pick nums[i]
    if nums[i] % 3 = 0
        dp[i][0] = dp[i-1][0] + nums[i]
        dp[i][1] = dp[i-1][1] + nums[i]
        dp[i][2] = dp[i-1][2] + nums[i]

    if nums[i] % 3 = 1
        dp[i][0] = dp[i-1][2] + nums[i]
        dp[i][1] = dp[i-1][0] + nums[i]
        dp[i][2] = dp[i-1][1] + nums[i]

    if nums[i] % 3 = 2
        dp[i][0] = dp[i-1][1] + nums[i]
        dp[i][1] = dp[i-1][2] + nums[i]
        dp[i][2] = dp[i-1][1] + nums[i]

2. do not pick nums[i]
        dp[i][j] = d[i-1][j]

or
if total % 3 == 0: return all
if total % 3 == 1:
    delete one mod 3 == 1
    delete two mod 3 == 2
    delete one mod 3 == 2 and two mod 3 == 1

if total % 3 == 2:
    delete one mod 3 == 1
    delete two mod 3 == 2
    delete two mod 3 == 2 and one mod 3 == 1



"""

import functools

class Solution:
    def maxSumDivThree(self, nums) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, remain):
            if i == n:
                if remain == 0:
                    return 0
                else:
                    return -float("inf")

            new_remain = (remain + nums[i] % 3) % 3
            return max(dfs(i + 1, remain), dfs(i + 1, new_remain) + nums[i])

        return dfs(0, 0)




class Solution2:
    def maxSumDivThree(self, nums) -> int:
        memo = {}
        return self.dfs(nums, 0, 0, memo)

    def dfs(self, nums, i, remain, memo):
        if (i, remain) in memo:
            return memo[(i, remain)]

        n = len(nums)
        if i == n:
            if remain == 0:
                return 0
            else:
                return -float("inf")

        new_remain = (remain + nums[i] % 3) % 3
        memo[(i, remain)] = max(self.dfs(nums, i + 1, remain, memo), self.dfs(nums, i + 1, new_remain, memo) + nums[i])
        return memo[(i, remain)]

