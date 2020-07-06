
"""
A(x1, y1)           (x2, y1)
(x1, y2)            B(x2, y2)

找到AB基本CD也就确定了

for A =
    for B =
        if (C, D) in set:
            area =
            res = min(res, area)

"""


class Solution:
    def minAreaRect(self, points) -> int:
        visited = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    res = min(res, area)
            visited.add((x1, y1))
        return res if res < float('inf') else 0


