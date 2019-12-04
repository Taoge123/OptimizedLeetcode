

"""
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).



Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words,
we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.


Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:
"""


class Solution:
    def isConvex(self, points) -> bool:

        n = len(points)
        crossProduct = None

        for i in range(-2, n - 2):
            x = [points[i][0], points[i + 1][0], points[i + 2][0]]
            y = [points[i][1], points[i + 1][1], points[i + 2][1]]

            dx1 = x[1] - x[0]
            dy1 = y[1] - y[0]

            dx2 = x[2] - x[1]
            dy2 = y[2] - y[1]

            temp = dx1 * dy2 - dy1 * dx2

            if not crossProduct:
                crossProduct = temp

            elif (temp) * crossProduct < 0:
                return False

        return True







