"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""



class Solution:
    def summaryRanges(self, nums):
        i, j = 0, 0
        res = []
        while i < len(nums) and j < len(nums):
            k = 0
            while j < len(nums) and nums[i] + k == nums[j]:
                j += 1
                k += 1
            if j == i + 1:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + '->' + str(nums[j-1]))
            i = j
        return res


nums1 = [0,1,2,4,5,7]
nums2 = [0,2,3,4,6,8,9]

a = Solution()
print(a.summaryRanges(nums1))



