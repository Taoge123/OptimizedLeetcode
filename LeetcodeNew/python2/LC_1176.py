
class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        res = 0
        cur = sum(calories[0:k])

        if cur > upper:
            res += 1
        if cur < lower:
            res -= 1

        for i in range(k, len(calories)):
            cur += calories[i] - calories[i - k]
            if cur > upper:
                res += 1
            elif cur < lower:
                res -= 1

        return res



