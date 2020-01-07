"""
315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""


import bisect
class Solution:
    def reversePairs(self, nums) -> int:
        res = 0
        arr = []
        for i in range(len(nums)):
            index = bisect.bisect_right(arr, 2 * nums[i])
            res += (i - index)
            bisect.insort(arr, nums[i])
        return res


class Solution2:
    def __init__(self):
        self.res = 0

    def reversePairs(self, nums):
        self.mergeSort(nums)
        return self.res

    def mergeSort(self, nums):
        # merge sort body
        n = len(nums)
        if n <= 1:  # base case
            return nums
        else:  # recursive case
            left = self.mergeSort(nums[:int(n / 2)])
            right = self.mergeSort(nums[int(n / 2):])
            return self.merge(left, right)

    def merge(self, left, right):
        # merge
        i, j = 0, 0  # increase l and r iteratively
        while i < len(left) and j < len(right):
            if left[i] <= 2 * right[j]:
                i += 1
            else:
                self.res += len(left) - i  # add here
                j += 1
        return sorted(left + right)  # I can't avoid TLE without timsort...




class Solution3:
    def reversePairs(self, nums):
        if len(nums) <= 1:
            return 0
        res = [0]
        self.merge(nums, res)
        return res[0]

    def merge(self, nums, res):
        if len(nums) <= 1:
            return nums

        left = self.merge(nums[:len(nums) // 2], res)
        right = self.merge(nums[len(nums) // 2:], res)
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= 2 * right[j]:
                i += 1
            else:
                res[0] += len(left) - i
                j += 1

        return sorted(left + right)




