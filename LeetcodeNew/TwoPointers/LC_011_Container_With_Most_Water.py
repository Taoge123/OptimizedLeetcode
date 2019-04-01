
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

"""
If height[L] < height[R], move L, else move R. Say height[0] < height[5], 
area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.
"""

class Solution1:
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res


class Solution2:
    def maxArea(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res

"""
Since we know area = length * min (height_a, height_b),
 to maximize the area we want to maximize both height and length.

- Width: We set two pointers, which are initialized as 0 and len(height) - 1 to get the max width.
- Height: We move the left pointer and right pointer respectively to search for the next higher height.
"""

class Solution3:
    def maxArea(self, height):
        max_area = area = 0
        left, right = 0, len(height) - 1
        while left < right:
            l, r = height[left], height[right]
            if l < r:
                area = (right - left) * l
                while height[left] <= l:
                    left += 1
            else:
                area = (right - left) * r
                while height[right] <= r and right:
                    right -= 1
            if area > max_area:
                max_area = area
        return max_area


"""
Start with the widest possible container where endpoints are the first and last entries in height. 
Keep track of the max area seen thus far and converge towards the narrowest container.
"""

class Solution5:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_area

