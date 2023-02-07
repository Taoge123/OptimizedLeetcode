"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

"""

import collections

class Solution:
    def numberOfBoomerangs(self, nums) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            table = collections.defaultdict(int)
            for j in range(n):
                dx = nums[i][0] - nums[j][0]
                dy = nums[i][1] - nums[j][1]
                dist = dx ** 2 + dy ** 2
                table[dist] += 1

            for val in table.values():
                res += (val - 1) * val
        return res



points = [[0,0],[1,0],[2,0]]
a = Solution()
print(a.numberOfBoomerangs(points))




