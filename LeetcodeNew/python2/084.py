

class Solution:
    def largestRectangleArea(self, heights):

        res = 0
        stack = [-1]
        heights.append(0)

        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                high = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, high * width)
            stack.append(i)
        return res






