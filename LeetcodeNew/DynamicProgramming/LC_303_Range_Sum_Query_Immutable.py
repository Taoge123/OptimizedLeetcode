
"""
https://leetcode.com/problems/range-sum-query-immutable/solution/


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""
"""
The idea is fairly straightforward: 
create an array accu that stores the accumulated sum for nums 
such that accu[i] = nums[0] + ... + nums[i - 1] in the initializer of NumArray. 
Then just return accu[j + 1] - accu[i] in sumRange. 
You may try the example in the problem statement to convince yourself of this idea.
"""

class NumArray1:
    def __init__(self, nums):

        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        # sum of elements nums[i..j], inclusive.
        return self.accu[j + 1] - self.accu[i]



class NumArray2:
    def __init__(self, nums):
        self.dc = {-1:0}
        for i,v in enumerate(nums):
            self.dc[i] = self.dc[i-1] + v

    def sumRange(self, i, j):
        return self.dc[j]-self.dc[i-1]

