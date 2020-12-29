"""
https://www.youtube.com/watch?v=8IX9j5WLLD4
"""

import math

class Solution:
    def getMinDistSum(self, positions) -> float:

        def dist(i, j):
            res = 0
            for x, y in positions:
                res += math.sqrt((x - i) ** 2 + (y - j) ** 2)
            return res

        step = 1
        n = len(positions)
        sx, sy = 0, 0
        #         for x, y in positions:
        #             sx += x
        #             sy += y

        #         sx /= n
        #         sy /= n

        res = dist(sx, sy)

        while step > 0.000001:
            flag = True
            for dx, dy in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                tx = sx + dx
                ty = sy + dy
                newDist = dist(tx, ty)
                if newDist < res:
                    res = newDist
                    sx, sy = tx, ty
                    flag = False

            if flag:
                step /= 10

        return res


