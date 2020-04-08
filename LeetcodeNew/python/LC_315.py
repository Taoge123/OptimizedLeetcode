"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/408322/Python-Different-Concise-Solutions

315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

You are given an integer array nums and you have to return a new counts array.
he counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
import bisect

class Solution:
    def countSmaller(self, nums):
        arr = []
        res = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(arr, num)
            res.append(idx)
            arr.insert(idx, num)
        return res[::-1]


class Solution2:
    def countSmaller(self, nums):
        nums = nums[::-1]
        nums = [(num, i) for i, num in enumerate(nums)]
        res = [0] * len(nums)

        self.mergesort(nums, 0, len(nums) - 1, res) if nums else None
        return res[::-1]

    def mergesort(self, nums, left, right, res):
        if left == right:
            return
        mid = (left + right) // 2
        self.mergesort(nums, left, mid, res)
        self.mergesort(nums, mid + 1, right, res)

        i = left
        # O(n)
        for j in range(mid + 1, right + 1):
            while i < mid + 1 and nums[i][0] < nums[j][0]:
                i += 1
            res[nums[j][1]] += i - left
        nums[left:right + 1] = sorted(nums[left:right + 1])



