"""
https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/663791/Python-DP-detailed-explanation

Don't directly calculate probability. Calculate the number of "success count" instead. After getting total "success count", probability can be obtained using "success count / total count". Where "total count" equals the combinations of "taking half balls out of all balls", which is a mathmatical problem: "comb(n, n//2)". (python provides "comb" function out of the box).

We allocate balls into two buckets, with first bucket having balls count "num1", distinct colors count "c1", and second bucket having balls count "num2" and distinct colors count "c2". When we see "num1==num2==totalBalls//2 and c1==c2" at the same time, we find one success count.
dp(i, num1, c1, num2, c2): "i" means the index in balls[i]. dp returns the "success count" at and after index "i". "num1, num2, c1, c2" are the bucket states of index "i-1".

In dp, we loop through all different ways allocating "balls[i]" to bucket1 and bucket2. Be careful that if we decide to allocate some balls to bucket1, for example "two" balls, then the "two" balls can be choosen from all different balls in "balls[i]". That's why there is a "comb" statement inside the "for" loop in dp.

Time complexity: O(totalColors * totalBalls^2 * totalColors^2 * maxBallEachColor )
Without "@functools.lru_cache(None)": 3000ms
With "@functools.lru_cache(None)": 30ms

"""

import math
import functools

class Solution:
    def getProbability(self, balls) -> float:

        @functools.lru_cache(None)
        def dfs(i, num1, count1, num2, count2):
            if num1 > totalBalls // 2 or num2 > totalBalls // 2:
                return 0
            if i >= len(balls):
                if num1 == num2 == totalBalls // 2 and count1 == count2:
                    return True
                else:
                    return False

            res = 0
            for bucket1 in range(balls[i] + 1):
                bucket2 = balls[i] - bucket1
                ways = math.comb(balls[i], bucket1)
                successCount = dfs(i + 1, num1 + bucket1, count1 + (bucket1 != 0), num2 + bucket2, count2 + (bucket2 != 0))
                res += successCount * ways
            return res

        totalBalls = sum(balls)
        return dfs(0, 0, 0, 0, 0) / math.comb(totalBalls, totalBalls // 2)

