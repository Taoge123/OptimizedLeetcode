
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

import collections

class SolutionCounter:
    def intersect(self, nums1, nums2):
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        result = []
        for n in c1:
            if n in c2:
                result += [n] * min(c1[n], c2[n])
        return result

class Solution:
    def intersect(self, nums1, nums2):
        res, freq = [], collections.defaultdict(int)
        for n in nums1:
            freq[n] += 1
        for n in nums2:
            if freq[n] > 0:
                res.append(n)
                freq[n] -= 1
        return res

class Solution11:
    def intersect(self, nums1, nums2):

        nums1.sort()
        nums2.sort()
        res = []
        a = 0
        b = 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                res.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        return res

# two pointers:
class Solution1:
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

# use dictionary to count:
class Solution2:
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res

# use Counter to make it cleaner:
class Solution3:
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res







