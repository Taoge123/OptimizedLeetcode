"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""
"""
[1, -1, 5, -2, 3], k = 3
 1,  0, 5,  3, 6
 
 0 -1
 1  0
 //0 1
 5  1
 3  2
 6  3

basic idea is not to update the dic since we are looking for max instead of min

"""

class Solution:
    def maxSubArrayLen(self, nums, k: int) -> int:
        res = 0
        summ = 0
        table = {0 : -1}
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in table:
                res = max(res, i - table[summ - k])
            #we dont update the table since we want to have max
            if summ not in table:
                table[summ] = i
        return res



nums = [1, 1, 1, 1, 1]
k = 3

a = Solution()
print(a.maxSubArrayLen(nums, k))



