"""
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height):

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
                left += 1

            else:
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
                right -= 1

        return res


class SolutionStack:
    def trap(self, height) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if not stack:
                    continue
                # 看pop的左右边哪个小 - 刚pop出去的
                h = min(height[stack[-1]], height[i]) - base
                w = i - stack[-1] - 1
                res += w * h
            stack.append(i)
        return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]

a = Solution()
print(a.trap(height))



