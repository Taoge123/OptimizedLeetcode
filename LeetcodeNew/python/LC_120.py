"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

import functools


class Solutiontony:
    def minimumTotal(self, triangle) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == len(triangle):
                return 0

            left = triangle[i][j] + dfs(i + 1, j)
            right = triangle[i][j] + dfs(i + 1, j + 1)
            return min(left, right)

        return dfs(0, 0)




class Solution:
    def minimumTotal(self, triangle):

        if not triangle:
            return

        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])



class Solution2:
    def minimumTotal(self, triangle):
        res = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                res[i] = row[i] + min(res[i], res[i +1])
        return res[0]









