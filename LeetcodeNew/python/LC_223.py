"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.

"""
"""
223.Rectangle-Area
整体而言这是一个容斥原理的应用。A并B = A + B - A交B

其中“A交B”的面积计算，通过确定相交区域的左下角和右上角来得到。

x_left_bottom = max(x1_left_bottom, x2_left_bottom)
y_left_bottom = max(y1_left_bottom, y2_left_bottom)
x_right_top = min(x1_right_top, x2_right_top)
y_right_top = min(y1_right_top, y2_right_top)
特别注意要检查 x_left_bottom < x_right_top和 y_left_bottom < y_right_top，才能说明有真正意义的相交矩形。
"""

class SolutionTony:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        x1 = max(A, E)
        y1 = max(B, F)

        x2 = min(C, G)
        y2 = min(D, H)
        if x2 - x1 < 0 or y2 - y1 < 0:
            overlap = 0
        else:
            overlap = max((x2 - x1) * (y2 - y1), 0)

        return (C - A) * (D - B) + (G - E) * (H - F) - overlap


class SolutionRika:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rectangle1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        rectangle2 = abs(bx1 - bx2) * abs(by1 - by2)

        w = max(0, min(ax2, bx2) - max(ax1, bx1))  # if w < 0, no intersection
        h = max(0, min(ay2, by2) - max(ay1, by1))  # if h <0, no intersection

        overlap = w * h

        return rectangle1 + rectangle2 - overlap


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        area1 = abs(C - A) * abs(B - D)
        area2 = abs(E - G) * abs(F - H)
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        if w <= 0 or h <= 0:
            return area1 + area2
        else:
            return area1 + area2 - w * h






