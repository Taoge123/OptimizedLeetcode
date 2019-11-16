
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        start, end = 0, nums[0]
        res = 1
        while end < len(nums) - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(start, end + 1))
            start, end = end, nxt
        return res




