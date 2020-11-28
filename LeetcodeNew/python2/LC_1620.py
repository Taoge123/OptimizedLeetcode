import math

class Solution:
    def bestCoordinate(self, towers, radius: int):
        maxSQ = 0
        res = [0, 0]

        for x in range(51):
            for y in range(51):
                quality = 0
                for i, j, q in towers:
                    xd = x - i
                    yd = y - j
                    dist = math.sqrt(xd * xd + yd * yd)

                    if dist <= radius:
                        quality += q // (1 + dist)

                if quality > maxSQ:
                    maxSQ = quality
                    res = [x, y]

        return res



