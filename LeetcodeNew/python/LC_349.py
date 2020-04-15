"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


class Solution2:
    def intersection(self, nums1, nums2):
        res = set()
        num
        for num in nums1:
            temp = self.search(nums2, num)
            if temp != -1:
                res.add(temp)
        return list(res)

    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return target
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1



nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]


a = Solution2()
print(a.intersection(nums1, nums2))



