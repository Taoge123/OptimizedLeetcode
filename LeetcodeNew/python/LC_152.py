"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class SolutionTony:
    def maxProduct(self, nums) -> int:
        res = nums[0]
        mini, maxi = nums[0], nums[0]
        for i in range(1, len(nums)):
            newMax = max(nums[i], maxi * nums[i], mini * nums[i])
            newMin = min(nums[i], maxi * nums[i], mini * nums[i])
            maxi, mini = newMax, newMin
            res = max(res, maxi)
        return res




class Solution:
    def maxProduct(self, nums):
        mini = maxi = res = nums[0]

        for num in nums[1:]:
            temp = maxi
            maxi = max(max(maxi * num, mini * num), num)
            mini = min(min(mini * num, temp * num), num)
            res = max(res, maxi)
        return res



