"""
http://www.jeffreythompson.org/collision-detection/circle-rect.php
https://leetcode.com/problems/circle-and-rectangle-overlapping/discuss/580034/Python%3A-explanation-with-figures
"""


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the nearest point on the rectangle to the center of the circle
        x_nearest = max(x1, min(x_center, x2))
        y_nearest = max(y1, min(y_center, y2))

        # Find the distance between the nearest point and the center of the circle
        # Distance between 2 points, (x1,y1) & (x2,y2) in 2D Euclidean space = ((x1-x2)**2 + (y1-y2)**2)**0.5
        distance_x = x_nearest - x_center
        distance_y = y_nearest - y_center
        return (distance_x ** 2 + distance_y ** 2) <= radius ** 2







