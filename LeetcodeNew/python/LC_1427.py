
class Solution:
    def stringShift(self, s: str, shift) -> str:
        step = 0
        for x, y in shift:
            if x == 0:
                step -= y
            else:
                step += y

        step %= len(s)
        return s[-step:] + s[:-step]


