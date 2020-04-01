"""
up =
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]

2 3 4
4 5 6 7

case 1: k < min(len1, len2)
k = 0 3
k = 1 2
k = 2 1
k = 3 0

case 2:

case 3: k > max(len1, len2) + 1 - return -1




"""



class Solution:
    def maxNumber(self, nums1, nums2, k):
        n, m= len(nums1), len(nums2)
        ret = [0] * k
        for i in range(0, k + 1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret

    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n: return ret
        while selects > 0:
            start = ret[-1] + 1  # search start
            end = n - selects + 1  # search end
            ret.append(max(range(start, end), key=nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret





