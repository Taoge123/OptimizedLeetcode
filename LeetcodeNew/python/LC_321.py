"""
similar to 358

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

"""
K < min(len(s1,s2))
S1 + s2 = n
max()
s1 + s2 - (k-1)
4 + 6 - 4 = 6
K = 5
3465  => min(4, 6)
912583 => min(6, 6)
K = 5
135  =  min(3, 4)
24689 = min(5, 4) = 4  max(s2[:4])
8 - (5-1) = 4
l1, l2 = len(nums1), len(nums2)
reserve = l1 + l2 - (k-1)
Greedy: temp =  max(max(nums1[:min(l1, reserve)]),   max(nums2[:min(l2, reserve)]))
min(temp, up[0])
135
9
L1 + l2 == k
9 135
89135
ans[i]
Up[i]

I+ 1 has up
Up[i] > ans[i]
3456
29
K > l1 + l2


"""


class SolutionTonnie:
    def maxNumber(self, nums1, nums2, k):
        def mostCompetitive(nums, k):
            k = len(nums) - k
            if k >= len(nums):
                return []
            stack = []
            for num in nums:
                while stack and k and stack[-1] < num:
                    stack.pop()
                    k -= 1
                stack.append(num)

            while stack and k:
                stack.pop()
                k -= 1
            return stack

        def mergeMax(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res += nums1[0],
                    nums1 = nums1[1:]
                else:
                    res += nums2[0],
                    nums2 = nums2[1:]
            return res

        m, n = len(nums1), len(nums2)
        res = [0] * k
        for i in range(0, k + 1):
            j = k - i
            if i > m or j > n:
                continue
            left = mostCompetitive(nums1, i)
            right = mostCompetitive(nums2, j)
            num = mergeMax(left, right)
            res = max(num, res)
        return res



class SolutionTony:
    def maxNumber(self, nums1, nums2, k):
        n, m = len(nums1), len(nums2)
        res = [0] * k
        for i in range(0, k + 1):
            j = k - i
            if i > n or j > m:
                continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            res = max(num, res)
        return res

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
        res = [-1]
        if selects > n: return res
        while selects > 0:
            start = res[-1] + 1  # search start
            end = n - selects + 1  # search end
            res.append(max(range(start, end), key=nums.__getitem__))
            selects -= 1
        res = [nums[item] for item in res[1:]]
        return res




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





