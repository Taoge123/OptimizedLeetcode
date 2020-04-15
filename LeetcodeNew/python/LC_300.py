"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""

import bisect

class Solution:
    def lengthOfLIS(self, nums):

        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)



class SolutionTest:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = []
        for i, num in enumerate(nums):
            index = self.bisect_left(dp, num)
            if index >= len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)

    def bisect_left(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


"""
  [1, 3, 6, 7, 9, 4, 10, 5, 6]
               i 

   1. 2. 3. 4. 5. 3. 6.  3. 5

if nums[j] > nums[i]:
    dp[j] = max(dp[i] + 1, dp[j])
else:


"""







