"""
209 Minimum Size Subarray Sum
862 Shortest Subarray with Sum at Least K
904 Fruit Into Baskets
930 Binary Subarrays With Sum
992 Subarrays with K Different Integers
1004 Max Consecutive Ones III
1234 Replace the Substring for Balanced String
1248 Count Number of Nice Subarrays
1358 Number of Substrings Containing All Three Characters
1425 Constrained Subsequence Sum
1493 Longest Subarray of 1's After Deleting One Element

"""


class Solution:
    def longestSubarray(self, nums) -> int:
        res = 0
        left, summ = 0, 0
        for right, num in enumerate(nums):
            summ += num
            if summ < right - left:
                summ -= nums[left]
                left += 1
            res = max(res, right - left)
        return res



