
"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""

import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        res = []
        window = sorted(nums[:k])
        res.append(self.median(window, k))
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            bisect.insort(window, nums[i])
            res.append(self.median(window, k))
        return res

    def median(self, window, k):
        if k % 2:
            return float(window[k // 2])
        else:
            return (window[k // 2] + window[k // 2 - 1]) / 2.0



class SolutionTony:
    def medianSlidingWindow(self, nums, k: int):

        n = len(nums)
        res = []
        for right in range(n + 1):
            window = []
            if right >= k:
                window = sorted(nums[right - k:right])
                m = len(window)
                if len(window) % 2 == 0:
                    mid = (window[m // 2] + window[m // 2 - 1]) / 2
                    res.append(mid)
                else:
                    res.append(window[m // 2])
        return res




nums = [1,3,-1,-3,5,3,6,7]
a = Solution()
print(a.medianSlidingWindow(nums, 3))
