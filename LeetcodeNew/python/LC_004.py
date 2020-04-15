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


"""
--------- ma -----------
---------------- mb ------------------


"""



class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        l = n1 + n2
        if l % 2 == 1:
            return self.find(nums1, 0, n1 - 1, nums2, 0, n2 - 1, l // 2)
        else:
            return (self.find(nums1, 0, n1 - 1, nums2, 0, n2 - 1, l // 2)
                    + self.find(nums1, 0, n1 - 1, nums2, 0, n2 - 1, l // 2 - 1)) / 2.0

    def find(self, nums1, s1, e1, nums2, s2, e2, k):
        if e1 - s1 < 0:
            return nums2[k + s2]
        if e2 - s2 < 0:
            return nums1[k + s1]
        if k < 1:
            return min(nums1[k + s1], nums2[k + s2])

        ia, ib = (s1 + e1) // 2, (s2 + e2) // 2
        ma, mb = nums1[ia], nums2[ib]

        #如果两个数组左半段之和还是小于k，删除小的左半段，k也要减去删除size的大小
        if (ia - s1) + (ib - s2) < k:
            if ma > mb:
                return self.find(nums1, s1, e1, nums2, ib + 1, e2, k - (ib - s2) - 1)
            else:
                return self.find(nums1, ia + 1, e1, nums2, s2, e2, k - (ia - s1) - 1)
        # 相反删右边，k不变
        else:
            if ma > mb:
                return self.find(nums1, s1, ia - 1, nums2, s2, e2, k)
            else:
                return self.find(nums1, s1, e1, nums2, s2, ib - 1, k)




