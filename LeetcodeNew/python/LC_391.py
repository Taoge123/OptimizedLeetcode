
"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example,
a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.

"""


class Solution:
    def isRectangleCover(self, rectangles) -> bool:

        area = 0
        corners = set()

        for p0, p1, p2, p3 in rectangles:
            fours = [(p0, p1), (p0, p3), (p2, p1), (p2, p3)]
            for point in fours:
                if point not in corners:
                    corners.add(point)
                else:
                    corners.remove(point)
            area += (p3 - p1) * (p2 - p0)

        if len(corners) != 4:
            return False

        corners = sorted(corners, key=lambda x: (x[0], x[1]))

        if (corners[3][0] - corners[1][0]) * (corners[3][1] - corners[2][1]) != area:
            return False
        return True


class Solution2:
    def isRectangleCover(self, rectangles):
        if len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")
        corners = set()
        area = 0
        for p0, p1, p2, p3 in rectangles:
            x1 = min(p0, x1)
            y1 = min(p1, y1)
            x2 = max(p2, x2)
            y2 = max(p3, y2)
            area += (p3 - p1) * (p2 - p0)
            corners.remove((p0, p3)) if (p0, p3) in corners else corners.add((p0, p3))
            corners.remove((p0, p1)) if (p0, p1) in corners else corners.add((p0, p1))
            corners.remove((p2, p3)) if (p2, p3) in corners else corners.add((p2, p3))
            corners.remove((p2, p1)) if (p2, p1) in corners else corners.add((p2, p1))
        if (x1, y2) not in corners or (x2, y1) not in corners or (x1, y1) not in corners \
                or (x2, y2) not in corners or len(corners) != 4:
            return False
        return area == (y2 - y1) * (x2 - x1)



rectangles = [[1,1,3,3],
              [3,1,4,2],
              [3,2,4,4],
              [1,3,2,4],
              [2,3,3,4]]

a = Solution()
print(a.isRectangleCover(rectangles))











