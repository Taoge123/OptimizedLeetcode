
"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""


class SolutionTony:
    def findMaxLength(self, nums) -> int:
        nums = [1 if num == 1 else -1 for num in nums]
        summ = 0
        n = len(nums)
        res = 0
        table = {}
        table[0] = -1
        for right in range(n):
            summ += nums[right]
            if summ in table:
                res = max(res, right - table[summ])
            else:
                table[summ] = right
        return res


# nums = [0,1,0,1]
# a = Solution()
# print(a.findMaxLength(nums))


class Solution:
    def findMaxLength(self, nums) -> int:

        table = {}
        table[0] = -1
        res = 0
        count = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i
        return res






