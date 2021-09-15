
"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""

"""
410. Split Array Largest Sum
774. Minimize Max Distance to Gas Station
875. Koko Eating Bananas
1011. Capacity To Ship Packages Within D Days
1231. Divide Chocolate
1201. Ugly Number III
"""

import functools

class Solution:
    def splitArray(self, nums, m):
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        @functools.lru_cache(None)
        def dfs(pos, m):
            if pos == len(nums):
                return 0 if m == 0 else float('inf')

            res = float('inf')
            total = 0
            for i in range(pos, len(nums)):
                total = presum[i + 1] - presum[pos]
                res = min(res, max(total, dfs(i + 1, m - 1)))
            return res

        return dfs(0, m)


class SolutionTony:
    def splitArray(self, nums, m: int) -> int:
        left, right = max(nums), sum(nums) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.search(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left

    def search(self, nums, mid):
        count = 1
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > mid:
                count += 1
                curSum = num
        return count




class Solution:
    def splitArray(self, nums, m: int) -> int:
        self.m = m
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if self.valid(nums, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def valid(self, nums, mid):
        count = 0
        summ = 0
        for num in nums:
            summ += num
            if summ > mid:
                summ = num
                count += 1
                if count >= self.m:
                    return False
        return True




"""

XXX X XXXXXXXXXXXXx
i   k   j    
解法1: DP
大多数的数组问题都可以用动态规划解决。

设计dp[i][k]表示元素1~i分成k份的最佳方案，即最大子区段的最小可能值。

如何设计转移方程呢？无非就是考虑dp[i][k]和这些前态的关系：dp[i-？][k], dp[i][k-？]。
可以发现，dp[i][k]和dp[i-1][k-1]有直接关系。遍历所有将前j个元素（j最小就是k-1）分成k-1份的方案，加上最后一份（就是 sum[i]-sum[j]）的影响。

所以转移方程是： dp[i][k]=min{j} ( max(dp[j][k-1],sum[i]-sum[j]) )

注意的细节是，sum[i]的计算可能会溢出。sum[i]-sum[j]可以转化为 dp[i][1]-dp[j][1].
"""


class SolutionDP:
    def splitArray(self, nums, m: int) -> int:
        n = len(nums)
        dp = [[float('inf') for i in range(m + 1)] for j in range(n + 1)]
        summ = [0 for i in range(n + 1)]

        for i in range(n):
            summ[i + 1] = summ[i] + nums[i]

        dp[0][0] = 0
        for i in range(1, n + 1):
            for k in range(1, m + 1):
                for j in range(i):
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], summ[i] - summ[j]))

        return dp[n][m]




