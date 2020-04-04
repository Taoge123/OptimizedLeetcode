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
        m, n, result = len(nums1), len(nums2), []
        dp1, dp2 = self.maximize(nums1, m), self.maximize(nums2, n)

        for i in range(min(m + 1, k + 1)):
            if k - i not in dp2:
                continue
            temp = []
            for _ in range(k):
                if dp1[i] < dp2[k - i]:
                    temp.append(dp2[k - i].pop(0))
                else:
                    temp.append(dp1[i].pop(0))
            result = max(result, temp)
        return result

    def maximize(self, nums, length):
        dp, i = {length: nums}, 0
        while (length):
            while (i + 1 < length and nums[i] >= nums[i + 1]):
                i += 1
            nums, length = nums[:i] + nums[i + 1:], length - 1
            dp[length] = nums
            if i > 0: i -= 1
        return dp




class Solution2:
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





