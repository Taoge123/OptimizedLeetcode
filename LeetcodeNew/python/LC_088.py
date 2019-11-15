"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater
or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

class Solution:
    def merge(self, nums1, m, nums2, n):

        p = m - 1
        q = n - 1
        k = m + n - 1

        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[k] = nums1[p]
                k = k - 1
                p = p - 1
            else:
                nums1[k] = nums2[q]
                k = k - 1
                q = q - 1

        nums1[:q + 1] = nums2[:q + 1]


