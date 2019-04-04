
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
this is the answer from caikehe and all the comments below

the main idea is to iterate every number in nums.
we use the number as a target to find two other numbers which make total zero.
for those two other numbers, we move pointers, l and r, to try them.

l start from left to right
r start from right to left

first, we sort the array, so we can easily move i around and know how to adjust l and r.
if the number is the same as the number before, we have used it as target already, continue. [1]
we always start the left pointer from i+1 because the combination has already tried. [2]

now we calculate the total
if the total is less than zero, we need it to be larger, so we move the left pointer. [3]
if the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
if the total is zero, bingo! [5]
we need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]

we do not need to consider i after nums[i]>0, since sum of positive will be always greater than zero. [7]
we do not need to try the last two, since there are no rooms for l and r pointers.
You can think of it as The last two have been tried by all others. [8]

"""
class SolutionCaikehe:
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2): #[8]
			if nums[i]>0: break #[7]
			if i>0 and nums[i]==nums[i-1]: continue #[1]

			l, r = i+1, length-1 #[2]
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: #[3]
					l+=1
				elif total>0: #[4]
					r-=1
				else: #[5]
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: #[6]
						l+=1
					while l<r and nums[r]==nums[r-1]: #[6]
						r-=1
					l+=1
					r-=1
		return res

"""

大概思路是外围For一遍数组，然后在每次迭代的时候，设置[l,r]的区间，区间范围为l , r = i + 1, len(nums) - 1, 
这样比对的数就有3个，分别是nums[i], nums[l] 和 nums[r].
最终要达到的效果是: nums[l] + nums[r] == -nums[i]
这道题一定要记住去重，不仅仅是区间的l和r要去重，外围的i也需要去重。去重的方法如下:
i去重： if i == 0 or nums[i] > nums[i-1]:
l去重： while l < r and nums[l] == nums[l-1]: l += 1
r去重：while l < r and nums[r] == nums[r+1]: r -= 1

"""

class Solution2:
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res


"""
Solution with discussion https://discuss.leetcode.com/topic/75883/python-solution-with-detailed-explanation

3Sum https://leetcode.com/problems/3sum/

Sort based algorithm

a+b = -c. 3SUM reduces to 2SUM problem.
Handling Duplicates in 2SUM

Say index s and e are forming a solution in a sorted array. Now givens nums[s], 
there is a unique nums[e] such that nums[s]+nums[e]=Target. Therefore, if nums[s+1] is the same as nums[s], 
then searching in range s+1 to e will give us a duplicate solution. 
Thus we must move s till nums[s] != nums[s-1] to avoid getting duplicates.
                        while s<e and nums[s] == nums[s-1]:
                            s = s+1
Handling Duplicates in 3SUM

Imagine we are at index i and we have invoked the 2SUM problem from index i+1 to end of the array. 
Now once the 2SUM terminates, we will have a list of all triplets which include nums[i]. 
To avoid duplicates, we must skip all nums[i] where nums[i] == nums[i-1].
            if i > 0 and nums[i] == nums[i-1]:
                continue
"""

class Solution3:
    def threeSum(self, nums):

        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result






