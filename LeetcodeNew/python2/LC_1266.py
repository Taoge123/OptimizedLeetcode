
class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        res = 0

        for i in range(len(points) - 1):
            res += max(abs(points[i + 1][1] - points[i][1]), abs(points[i + 1][0] - points[i][0]))

        return res

