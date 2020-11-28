
class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        cur = 0
        res = 0
        for num in A:
            res = max(res, cur + num)
            cur = max(cur, num) - 1
        return res





