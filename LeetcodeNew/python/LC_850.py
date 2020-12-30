"""
https://leetcode.com/problems/rectangle-area-ii/discuss/707520/Python-Two-Clean-Solutions
"""

class Solution:
    def rectangleArea(self, rectangles) -> int:
        points = []
        for x1, y1, x2, y2 in rectangles:
            points.append((y1, x1, x2, True))
            points.append((y2, x1, x2, False))

        points.sort()
        res = 0
        intervals = []
        pre_y = points[0][0]
        width = 0

        for cur_y, x1, x2, is_start in points:
            h = cur_y - pre_y
            res += width * h

            if is_start:
                intervals.append((x1, x2))
            else:
                intervals.remove((x1, x2))  # replace with b-tree (self-balancing tree)

            width = self.helper(intervals)
            pre_y = cur_y

        return res % (10 ** 9 + 7)

    def helper(self, intervals):
        if len(intervals) == 0:
            return 0

        intervals.sort()
        end = intervals[0][1]
        res = intervals[0][1] - intervals[0][0]

        for x1, x2 in intervals[1:]:
            if end <= x1:
                res += x2 - x1
                end = x2
            elif end < x2:
                res += x2 - end
                end = x2

        return res

