"""
416. Partition Equal Subset Sum
473. Matchsticks to Square
698. Partition to K Equal Sum Subsets
996. Number of Squareful Arrays
"""
"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

https://github.com/wisdompeak/LeetCode/tree/master/DFS/698.Partition-to-K-Equal-Sum-Subsets
"""
import copy


class SolutionTony:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        nums.sort()
        memo = {}
        target = summ // 2

        return self.dfs(nums, 0, 0, target, memo)

    def dfs(self, nums, idx, summ, target, memo):
        if (summ, idx) in memo:
            return memo[(summ, idx)]

        if summ == target:
            return True

        if summ > target:
            return False

        for i in range(idx, len(nums)):
            if self.dfs(nums, i + 1, summ + nums[i], target, memo):
                memo[summ, idx] = True
                return memo[summ, idx]
        memo[summ, idx] = False
        return memo[summ, idx]



class Solution:
    def canPartition(self, nums) -> bool:

        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        visited = [False] * (len(nums))
        return self.dfs(nums, visited, 0, 0, target)

    def dfs(self, nums, visited, index, summ, target):
        if summ == target:
            return True
        if index == len(nums):
            return False
        if summ > target:
            return False

        for i in range(index, len(nums)):
            if visited[i] == True:
                continue
            visited[i] = True
            if i >= 1 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue
            if self.dfs(nums, visited, index + 1, summ + nums[i], target):
                return True
            visited[i] = False

        return False


"""
(100110) subset sum == summ // 2

s = subset sum
dp[s] : whether we can find a subset whose sum equals to s
0 ~ 2e4

dp[s_small] -> dp[s_large]

for num in nums:
    for s in range(summ//2+1):
        if dp[s-num] == True:
            dp[s] = True

"""


class SolutionWisdom:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False

        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            old_dp = copy.copy(dp)
            for i in range(target + 1):
                if i >= num:
                    dp[i] = dp[i] or old_dp[i - num]

        return dp[-1]


class SolutionReversed:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False

        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # old_dp = copy.copy(dp)
            for i in reversed(range(target + 1)):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]

        return dp[-1]


nums = [1, 5, 11, 5]
a = Solution()
print(a.canPartition(nums))







