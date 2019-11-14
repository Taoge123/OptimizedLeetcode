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


