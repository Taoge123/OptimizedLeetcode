"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""

import collections


class SolutionTony:
    def longestConsecutive(self, nums):

        n = len(nums)
        table = collections.Counter(nums)
        res = 0
        for i in range(n):
            # if we have smaller number already in table, then we can skip this one and compute later
            if nums[i] - 1 in table:
                continue
            count = 1
            num = nums[i] + 1
            while num in table:
                count += 1
                num += 1

            res = max(res, count)
        return res




class Solution:
    def longestConsecutive(self, nums):

        cache = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in cache:
                j = i
                while j in cache:
                    j += 1
                res = max(res, j - i)

        return res




class SolutionUF:
    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x != y:
            self.parent[y] = x
            self.size[x] += self.size[y]

    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        # remove the duplicate if any
        nums = set(nums)

        self.parent, self.size = {}, {}

        for num in nums:
            self.parent[num] = num
            self.size[num] = 1

        for n in nums:
            if n - 1 in nums:
                self.union(n, n - 1)
            if n + 1 in nums:
                self.union(n, n + 1)

        return max(self.size.values())





