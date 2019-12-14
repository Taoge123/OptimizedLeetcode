"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""



class Solution:
    def maximumGap(self, nums):
        # https://leetcode.com/problems/maximum-gap/discuss/330028/Explaining-the-bucket-method-in-layman-terms-%2B-python-code
        if len(nums) < 2 or min(nums) == max(nums):
            return 0

        mini, maxi = min(nums), max(nums)
        gap = (maxi - mini) // (len(nums) - 1) or 1

        bucket = [[None, None] for i in range((maxi - mini) // gap + 1)]

        for num in nums:
            b = (num - mini) // gap
            bucket[b][0] = num if bucket[b][0] is None else min(bucket[b][0], num)
            bucket[b][1] = num if bucket[b][1] is None else max(bucket[b][1], num)

        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))



nums = [3,6,9,1,17,19,28]
a = Solution()
print(a.maximumGap(nums))


