"""
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




