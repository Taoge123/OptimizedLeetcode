
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 360 / 12 * (hour % 12) + 360 / 12 / 60 * minutes
        m = 360 / 60 * minutes
        res = abs(h - m)
        return min(res, 360 - res)



class Solution2:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = 60 * hour + minutes
        res = (360 / 60 - 360 / 12 / 60) * m % 360
        return min(res, 360 - res)




