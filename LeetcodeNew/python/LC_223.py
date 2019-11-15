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






