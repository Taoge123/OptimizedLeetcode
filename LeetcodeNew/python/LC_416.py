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


class Solution2:
    def canPartition(self, nums):

        summ = sum(nums)
        if summ % 2:
            return False
        target = summ // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                print(i, i - num)
                dp[i] = dp[i] or dp[i - num]
        return dp[target]




nums = [1, 5, 11, 5]
a = Solution()
print(a.canPartition(nums))







