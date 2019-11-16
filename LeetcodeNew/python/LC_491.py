
"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.



Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]


Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""


# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         self.backTrack(nums, 0, [], res)
#         return list(res)

#     def backTrack(self, nums, index, path, res):
#         if len(path) > 1:
#             res.add(tuple(path))
#         if index == len(nums):
#             return
#         for i in range(index, len(nums)):
#             if not path or nums[i] >= path[-1]:
#                 path.append(nums[i])
#                 self.backTrack(nums, i + 1, path, res)
#                 path.pop()


class Solution:
    def findSubsequences(self, nums):
        res = set()
        self.backtrack(nums, 0, [], res)
        return list(res)

    def backtrack(self, nums, pos, path, res):
        if len(path) > 1:
            res.add(tuple(path))

        for i in range(pos, len(nums)):
            if not path or path[-1] <= nums[i]:
                self.backtrack(nums, i + 1, path + [nums[i]], res)




