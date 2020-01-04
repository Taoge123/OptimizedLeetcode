
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
"""


class Solution:
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







