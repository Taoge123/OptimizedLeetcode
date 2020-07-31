"""
812 Largest Triangle Area

(x1, y1), (x2, y1), (x3, y3)

(y3-y1)/(x3-x1) != (y2-y1)/(x2-x1)
(y3-y1)*(x2-x1) != (y2-y1)*(x3-x1)

"""


class SolutionWisdom:
    def isBoomerang(self, points) -> bool:
        x1 = points[0][0]
        x2 = points[1][0]
        x3 = points[2][0]
        y1 = points[0][1]
        y2 = points[1][1]
        y3 = points[2][1]
        return (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1)




class Solution:
    def isBoomerang(self, points) -> bool:
        a = points[1][1] - points[0][1]
        b = points[1][0] - points[0][0]
        c = points[2][1] - points[1][1]
        d = points[2][0] - points[1][0]
        return a * d != b * c

