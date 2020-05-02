

class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        count = [0] * 60
        res = 0
        for t in time:
            res += count[(60 - t) % 60]
            count[t % 60] += 1

        return res






