"""
https://maxming0.github.io/2020/05/17/Maximum-Number-of-Darts-Inside-of-a-Circular-Dartboard/
"""

import itertools

class Solution:
    def numPoints(self, points, r: int) -> int:

        res = 1
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            d = (x2 - x1) ** 2 + (y2 - y1) ** 2
            if d > 4 * r ** 2 or d == 0:
                continue

            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d / 4) ** 0.5 / d ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d / 4) ** 0.5 / d ** 0.5
            res = max(res, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))

            x0 = (x1 + x2) / 2.0 - (y2 - y1) * (r * r - d / 4) ** 0.5
            y0 = (y1 + y2) / 2.0 + (x2 - x1) * (r * r - d / 4) ** 0.5
            res = max(res, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))
        return res


