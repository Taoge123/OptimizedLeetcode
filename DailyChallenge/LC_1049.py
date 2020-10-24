

class Solution:
    def lastStoneWeightII(self, stones) -> int:

        dp = {0}
        for node in stones:
            newDP = dp
            dp = set()
            for x in newDP:
                dp.add(x + node)
                dp.add(x - node)

        res = float('inf')
        for num in dp:
            if num >= 0 and res > num:
                res = num

        return res


