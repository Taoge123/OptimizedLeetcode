"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2

    def kth(self, a, b, k):
        if not a:
            return b[k]

        if not b:
            return a[k]

        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        #we wanna search on the right becuz the k is larger and we are searching the smallest k
        if ia + ib < k:
            if ma < mb:
                #since we search on the right, and a < b, then we remove a's left, else b's left
                return self.kth(a[ia + 1:], b, k - ia - 1)
            else:
                return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            #Now k is less than the search, then we will search on the left, then we delete the larger part since we search on the left
            if ma < mb:  # now k is <= middle number index
                return self.kth(a, b[:ib], k)
            else:
                return self.kth(a[:ia], b, k)


