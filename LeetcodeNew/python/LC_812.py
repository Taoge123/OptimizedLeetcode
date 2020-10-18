import itertools

class Solution:
    def largestTriangleArea(self, points):
        def area(a, b, c):
            return .5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - c[1] * a[0])

        return max(area(*triangle) for triangle in itertools.combinations(points, 3))


class Solution2:
    def largestTriangleArea(self, points):
        def area(a, b, c):
            return .5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - c[1] * a[0])

        n = len(points)
        res = 0
        for i in points:
            for j in points:
                for k in points:
                    res = max(res, area(i, j, k))
        return res


