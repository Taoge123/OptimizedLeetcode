"""
812 Largest Triangle Area

"""


class Solution:
    def isBoomerang(self, points) -> bool:
        a = points[1][1] - points[0][1]
        b = points[1][0] - points[0][0]
        c = points[2][1] - points[1][1]
        d = points[2][0] - points[1][0]
        return a * d != b * c

