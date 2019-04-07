
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
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

class Solution1:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

"""
It's guaranteed to be O(log(min(m,n)) because every time the findKth function cuts the shorter array by half of its size.
"""


class Solution2:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)



class Solution3:
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2:  # the length is odd
            return self.findKthSmallest(nums1, nums2, l // 2 + 1)
        else:
            return (self.findKthSmallest(nums1, nums2, l // 2) + self.findKthSmallest(nums1, nums2, l // 2 + 1)) * 0.5

    def findKthSmallest(self, nums1, nums2, k):
        # force nums1 is not longer than nums2
        if len(nums1) > len(nums2):
            return self.findKthSmallest(nums2, nums1, k)
        if not nums1:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k / 2, len(nums1));
        pb = k - pa  # take care here
        if nums1[pa - 1] <= nums2[pb - 1]:
            return self.findKthSmallest(nums1[pa:], nums2, k - pa)
        else:
            return self.findKthSmallest(nums1, nums2[pb:], k - pb)


