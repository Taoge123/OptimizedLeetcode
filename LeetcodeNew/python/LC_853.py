
class Solution:
    def carFleet(self, target, position, speed):
        table = [float(target - pos) / s for pos, s in sorted(zip(position, speed))]
        cur = 0
        res = 0
        for time in table[::-1]:
            if time > cur:
                res += 1
                cur = time
        return res


