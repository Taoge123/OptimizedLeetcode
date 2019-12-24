"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n2) ?
"""


class Solution:
    def isReflected(self, points) -> bool:
        if not points:
            return True

        mini = min(i[0] for i in points)
        maxi = max(i[0] for i in points)
        table = set()
        for i in points:
            table.add(tuple(i))
        for i in points:
            if (mini + maxi - i[0], i[1]) not in table:
                return False
        return True


points = [[1,1],[-1,1]]
a = Solution()
print(a.isReflected(points))



