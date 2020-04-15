
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

import collections

class Solution:
    def intersect(self, nums1, nums2):

        count = collections.Counter(nums1)
        res = []
        for num in nums2:
            if count.get(num) and count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res


class Solution2:
    def intersect(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res





