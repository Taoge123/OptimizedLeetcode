"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

"""

class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    high = height[stack.pop()]
                    width = i - 1 - stack[i]
                    res = max(res, high * width)

                stack.append(i)
        return res







